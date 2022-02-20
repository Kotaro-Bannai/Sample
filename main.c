#include <stdio.h>
#include <math.h>
// #include <mkl.h>
#include "Parameter.h"
#include "selfconsistent.h"
#include "NewtonRaphson.h"

int main()
{
  // FILE *OUTPUT;
  // OUTPUT=fopen("mu_versus_phi.dat","w");

  Initialvalue(); //各パラメータ値の設定
  for(myu=-0.5;myu<3.5;myu+=0.001){
   phinew=1.0; //初期値
   NewtonRaphson(); //Newton法で解く
   printf("%12.9lf %12.9lf\n",myu/U,phinew); //データ表示
  //  fprintf(OUTPUT,"%12.9lf %12.9lf\n",myu/U,phinew); //データ書き込み
  }
  // fclose(OUTPUT);
}
