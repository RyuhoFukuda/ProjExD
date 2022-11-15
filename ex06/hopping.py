import pygame as pg
import sys                    
from random import randint

# 福田
sky = True #空にいるかどうかを判定するグローバル変数

# 福田,岡田
def collide(rct1, rct2): 
    #rct2が鳥、rct1が足場
    global sky           
    if rct2.top < rct1.top and rct2.bottom < rct1.bottom and rct2.colliderect(rct1):

        rct2.bottom = rct1.top
        sky = False
# 岡田
def draw_score(scr, time): #スコア画面
    fonto = pg.font.Font(None, 80)
    score = time // 1000
    txt = fonto.render(f"Score:{score}", True, "BLACK")
    scr.sfc.blit(txt, (10, 10))
# 泉
def start(scr): #スタート画面
    fonto = pg.font.Font(None, 60)
    txt = fonto.render("Press  SPACE  to  Start  Game", True, "BLACK")
    scr.sfc.blit(txt, (0,400))
        
# 福田
class Screen: #スクリーンクラス
    
    def __init__(self, title, wh, bg_file):
        pg.display.set_caption(title)
        self.wh = (wh[0], wh[1])
        self.sfc = pg.display.set_mode(self.wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bg_file)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        return self.sfc.blit(self.bgi_sfc, self.bgi_rct)

# 福田,岡田
class Bird: #こうかとん（操作可能キャラクター）クラス
# 福田,岡田
    def __init__(self, bird_path, zup, default):
        self.sfc = pg.image.load(bird_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zup)
        self.rct = self.sfc.get_rect()
        self.rct.center = default[0], default[1]

        self.speed_y = 0
        self.jump_power = 0
        self.charge = False

    def blit(self, scr :Screen):
        return scr.sfc.blit(self.sfc, self.rct)
# 岡田
    def update(self, scr :Screen):

        key_lst = pg.key.get_pressed()
        if sky == True:

            if key_lst[pg.K_LEFT]:
                self.rct.move_ip(-3, 0)
            if key_lst[pg.K_RIGHT]:
                self.rct.move_ip(+3, 0)
        self.wall_pass()
        self.blit(scr)

        #スピード制限
        if self.speed_y < 3:
            self.speed_y += 0.5

        #y軸に動かす
        self.rct.centery += self.speed_y
        
        pg.draw.rect(scr.sfc, (255, 0, 0), (self.rct.right, self.rct.centery, 20, 52))
        pg.draw.rect(scr.sfc, (255, 255, 255), (self.rct.right, self.rct.centery, 20, 52-self.jump_power*-3))
# 福田
    #壁と天井の判定
    def wall_pass(self):
        if self.rct.right < 0:
            self.rct.left = 600
        if self.rct.left > 600:
            self.rct.right = 0
        if self.rct.top < 0:
            self.rct.top = 0
# 岡田
    def jump(self, event):
        global sky
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_SPACE]:
            #スピード制限
            if self.jump_power > -20:
                self.jump_power -= 2

        #spacekeyを離したら跳ぶ
        if sky == False and event.type == pg.KEYUP:
            #少しの溜めでは跳ばない
            if self.jump_power > -1 :
                self.jump_power = 0
            else:
                sky = True
                self.speed_y += self.jump_power
                self.jump_power = 0
            
# 福田
class FootFold: #足場クラス

    global sky

    def __init__(self, y, scr :Screen):
        self.sfc = pg.Surface((125, 10))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.rect(self.sfc,(255, 0, 0),(0, 0, 125, 10))
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = y

    def blit(self, scr :Screen):
        return scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr :Screen):

        self.rct.centery += 1
        if self.rct.bottom > scr.rct.height:
            self.rct.centerx = randint(0, scr.rct.width)
            self.rct.bottom = 0
        self.blit(scr)       

# 福田
class Text: #テキスト表示クラス（だんだん近づいてくる機能付き）
            #今回は最終スコアの表示に使用

    def __init__(self, txt):
        self.txt = txt
        self.fonts = []
        for size in range(8, 300):
            self.fonts.append(pg.font.Font(None, size))

    def update(self, scr: Screen):
        for font in self.fonts:
            text = font.render(self.txt, True, (0,0,0))
            pos = font.size(self.txt)
            scr.blit()
            scr.sfc.blit(text, (int((scr.wh[0]-pos[0])/2),int((scr.wh[1]-pos[1])/2)))
            pg.display.update()
            pg.time.wait(30)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return

# 福田,岡田,泉
def main(): #メイン
    scr = Screen("飛べ！こうかとん", (600, 800), "ex06/aozora.jpg")
    bird = Bird("fig/3.png", 2.0, (300, 700))
    foot = FootFold(100, scr) #足場1
    foot1 = FootFold(300, scr) #足場2
    foot2 = FootFold(500, scr) #足場3
    foot3 = FootFold(700, scr) #足場4
    clock = pg.time.Clock() #時間
    starttime = True #最初の床が消えるかどうかの判定
    runflag = False #スタート画面とゲーム画面の判定

    # 泉
    while runflag == False: #スタート画面
        scr.blit()
        start(scr)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    runflag = True
    #福田, 岡田
    while (1): 
        scr.blit() #スクリーン貼り付け
        bird.update(scr) #こうかとんの更新
        foot.update(scr) #足場1の更新
        foot1.update(scr) #足場2の更新
        foot2.update(scr) #足場3の更新
        foot3.update(scr) #足場4の更新
        
        if starttime == True: #最初にのみ存在する足場
            first_box = pg.draw.rect(scr.sfc, (255,255,255), (250,780,100,10))
            collide(first_box, bird.rct) #最初にのみ存在する足場とこうかとんの衝突判定

        collide(foot.rct, bird.rct) #足場1とこうかとんの衝突判定
        collide(foot1.rct, bird.rct) #足場2とこうかとんの衝突判定
        collide(foot2.rct, bird.rct) #足場3とこうかとんの衝突判定
        collide(foot3.rct, bird.rct) #足場4とこうかとんの衝突判定

        for event in pg.event.get(): #イベント
                if event.type == pg.QUIT: #×ボタンを押したらゲームを終了する
                    return
                bird.jump(event) #こうかとんのジャンプについてのイベント

        if bird.rct.top > scr.rct.height: #こうかとんが画面外に出たらWhileを抜ける
            break

        time = pg.time.get_ticks() #時間
        draw_score(scr, time)
        pg.display.update() 
        clock.tick(120)
        if time >= 5000:
            starttime = False
    #福田
    while (1):
        gmov = Text(f"Score:{str(time // 1000)}") #最終スコアの表示
        gmov.update(scr) #最終スコア表示画面の更新
        return


if __name__ == "__main__":
    pg.init() # 初期化
    main()
    pg.quit()
    sys.exit()