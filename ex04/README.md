# 第4回
## 逃げろこうかとん
### ゲーム概要
* ex04/dodge_bomb.pyを実行すると,1400×700のスクリーンに背景が描画されて、こうかとんを移動することができる。同時に壁に当たると反射する爆弾である円が移動しているので、こうかとんが爆弾に当たらないようにする。
* こうかとんと爆弾が接触するとゲームオーバー。
### 操作方法
* 矢印キーでこうかとんを移動させる
### 追加機能
* 爆弾がこうかとんに接触した際に、遠くからGAMEOVERが近づいてくる機能を実装
* 爆弾がランダムに上から落下してくる機能を実装
* 爆弾が壁に当たって反射した際に爆弾が加速する機能を実装
* 無敵機能の実装：qキーを押している間だけ弾が当たっても無敵状態になれる機能を実装
* こうかとんを二人に増やしました。左のこうかとんはwasdキーで、右のこうかとんは矢印キーで移動できます。