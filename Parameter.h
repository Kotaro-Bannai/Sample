double phinew;    //超流動の秩序変数Φ
double z,J,U,myu; //各パラメータ
double Jmax=1.0; //Jの上限値

void Initialvalue(); //関数のプロトタイプ宣言

void Initialvalue()
{
  z = 1.0;   //最近接サイト数
  J = 0.04;  //ホッピング係数
  U = 1.0;   //オンサイト係数
  myu = 0.5; //化学ポテンシャル
}
