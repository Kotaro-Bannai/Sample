import openjij as oj
# import jijzept as jz
from pyqubo import Array
import numpy as np
from itertools import product

#スピンの割り当て(休暇：1、出勤：0)
x = Array.create('x',shape=(5,21),vartype='BINARY') #メインスピンx[0][0]~x[4][20] シフト人数×曜日数

#3次式チューニング後パラメータ
lamda1 = 0.965455; lamda2 = 0.636226; lamda3 = 0.593952; beta_min = 0.845216; beta_max = 49.883840

#1日に最低3人はシフトに入る(一日の休暇人数の1-hotで実装)
H1 = sum((1-(sum(x[i,j] for i in range(5))))**2 for j in range(21))

#全員1週目と2週目と3週目でそれぞれ2日は休む(各週の休暇日数の3-hotで実装)
H2 = sum((3-sum(x[i,j] for j in range(7)))**2 for i in range(5))\
   + sum((3-sum(x[i,j] for j in range(7,14)))**2 for i in range(5))\
   + sum((3-sum(x[i,j] for j in range(14,21)))**2 for i in range(5))

#3連休は禁止(高次式：ある起点から3連続で1(休み)が並ぶ場合のみコストが掛かる)
H3 = sum(sum(x[i,j]*x[i,j+1]*x[i,j+2] for j in range(19)) for i in range(5))

H = lamda1*H1 + lamda2*H2 + lamda3*H3

#QUBOモデル作成
model = H.compile()
qubo,offset = model.to_qubo()

#JijのSASamplerを用いてアニーリング
# sampler = jz.JijSASampler(config='/home/bannai/JijZept/config.toml')
sampler = oj.SASampler()

num_sweeps_list = [10, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]  #num_sweepsのリスト
num_annealing = 1000  #1回のアニーリングを行う回数
TTS_list = []  #各計算時間に対するTTSを格納しておくリスト
tau_list = []  #計算時間を格納しておくリスト
ps_list = []   #計算の過程で求まる成功確率を格納しておくリスト

for num_sweeps in num_sweeps_list:

    tau = 0  #1回のアニーリング時間
    valid = 0  #正解数

    responses = sampler.sample_qubo(qubo, num_reads=num_annealing, num_sweeps=num_sweeps, beta_min=beta_min, beta_max=beta_max)
    tau = responses.info['execution_time'] / 1000000
    # print(responses.info)

    #制約条件を満たしているかどうかを判定
    Rlist = []
    for s,e,o in responses.data(['sample', 'energy', 'num_occurrences']):
        Rlist.append(s)

    ans_list = [[] for i in range(num_annealing)]
    ans = [[] for i in range(num_annealing)]

    for k in range(num_annealing):
        for i in range(5):
            for j in range(21):
                ans_list[k].append(Rlist[k]['x[%d][%d]' % (i, j)])

        ans[k] = np.reshape(ans_list[k], (5, 21))

        cost_H1 = min(5-np.sum(ans[k],axis=0))
        cost_H2 = min([min(np.sum(ans[k][:,:7],axis=1)), min(np.sum(ans[k][:,7:14],axis=1)), min(np.sum(ans[k][:,14:21],axis=1))])
        cost_H3 = 0
        for i in range(5):
            for j in range(19):
                cost_H3 += ans[k][i][j]*ans[k][i][j+1]*ans[k][i][j+2]

        #制約条件を満たしている場合
        if cost_H1 >= 3 and cost_H2 >= 2 and cost_H3 == 0:
            valid += 1
            # print("All constraints are satisfied!")

        # print(ans[k])
        # print(5-np.sum(ans[k],axis=0))
        # print([min(np.sum(ans[k][:,:7],axis=1)), min(np.sum(ans[k][:,7:14],axis=1)), min(np.sum(ans[k][:,14:21],axis=1))])
        # print("cost_H1 =", cost_H1, end=" ")
        # print("cost_H2 =", cost_H2, end=" ")
        # print("cost_H3 =", cost_H3)

    #TTSの算出
    ps = valid/num_annealing
    pR = 0.99
    if ps == 0.0:
        ps = 1.0e-10
        print("ps = 0.0 when num_sweeps = %d"%(num_sweeps))
        # continue
    TTS_list.append(np.log(1-pR)/np.log(1-ps)*tau if ps < pR else tau)
    tau_list.append(tau)
    ps_list.append(ps)
    print("num_sweeps =",num_sweeps, end = " ")
    print("tau =",tau, end = " ")
    print("ps =",ps, end = " ")
    print("TTS =", np.log(1-pR)/np.log(1-ps)*tau if ps < pR else tau)

# print("TTS_list =", TTS_list)
# print("tau_list =",tau_list)
# print("ps_list =",ps_list)
