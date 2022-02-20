void NewtonRaphson(); //関数のプロトタイプ宣言

void NewtonRaphson()
{
  double delta1=1.0e-3;  //Newton法の刻み
  double delta2=1.0e-10; //収束判定条件
  double phiold1,phiold2;
  double f,fdelta,fprime;
  double norm;
  int i;

  // do{
  for(i=0;i<10;i+=1){
    // printf("%12.9lf\n",phinew);
    phiold1=phinew;
    selfconsistent();
    f=phinew-phiold1;
    norm=fabs(f);
    // printf("%12.9lf\n",phinew);

    // phinew=phiold1+delta1;
    // phiold2=phinew;
    // selfconsistent();
    // fdelta=phinew-phiold2;
    // fprime=(fdelta-f)/delta1;
    // phinew=phiold1-f/fprime;
  }
  // }while(norm>delta2);
}
