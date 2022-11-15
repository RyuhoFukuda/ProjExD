import pygame as pg
import sys
from random import randint

sky = 0

def collide(rct1, rct2): # 土台のRect、上に乗る鳥のRect、x速度、y速度
    global sky
    if rct1.top < rct2.bottom and rct1.bottom > rct2.top and rct1.left < rct2.right and rct1.right > rct2.left:
        sky = 1
        rct2.bottom = rct1.top

def start(scr): #泉追加分　スタート画面
    fonto = pg.font.Font(None, 60)
    txt = fonto.render("Press  SPACE  to  Start  Game", True, "BLACK")
    scr.sfc.blit(txt, (0,400))
        

class Screen:
    
    def __init__(self, title, wh, bg_file):
        pg.display.set_caption(title)
        self.wh = (wh[0], wh[1])
        self.sfc = pg.display.set_mode(self.wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bg_file)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        return self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:

    global sky

    def __init__(self, bird_path, zup, default):
        self.sfc = pg.image.load(bird_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zup)
        self.rct = self.sfc.get_rect()
        self.rct.center = default[0], default[1]
        self.vx = 0    #横方向の移動のための変数（着地したら0になる）
        self.vy = 0    #上方向にどのくらいいけるかを溜める溜めに使う変数
        self.vy2 = 1
    
    def blit(self, scr :Screen):
        return scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr :Screen):
        self.rct.move_ip(0, self.vy2)
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            self.vy += 1
        if sky == 0:
            if key_lst[pg.K_LEFT]:
                self.rct.move_ip(-1, 0)
            if key_lst[pg.K_RIGHT]:
                self.rct.move_ip(+1, 0)
        self.blit(scr)
    
class FootFold:

    def __init__(self, y, scr :Screen):
        self.sfc = pg.Surface((100, 20))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.rect(self.sfc,(255, 0, 0),(10, 10, 100, 10))
        self.rct = self.sfc.get_rect()
        self.y = y
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = self.y

    def blit(self, scr :Screen):
        return scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr :Screen):
        self.rct.move_ip(0, -1)
        if self.rct.bottom < 0:
            self.rct.centerx = randint(0, scr.rct.width)
            self.rct.bottom = scr.rct.height
        self.blit(scr)


def main():
    scr = Screen("飛べ！こうかとん", (600, 800), "ProjExD-1/ex04/pg_bg.jpg")
    bird = Bird("ProjExD-1/fig/1.png", 2.0, (300, 400))
    foot = FootFold(100, scr)
    foot1 = FootFold(300, scr)
    foot2 = FootFold(500, scr)
    runflag = False

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


    while runflag: #スタート画面から遷移した時にwhileに入る
        scr.blit()
        bird.update(scr)
        foot.update(scr)
        foot1.update(scr)
        foot2.update(scr)

        first_box = pg.draw.rect(scr.sfc, (255,255,255), (0,780,600,10))

        collide(foot.rct, bird.rct)
        collide(foot1.rct, bird.rct)
        collide(foot2.rct, bird.rct)
        collide(first_box, bird.rct)

        for event in pg.event.get():
                if event.type == pg.QUIT:
                    return

        pg.display.update() 
        clock = pg.time.Clock()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init() # 初期化
    main()
    pg.quit()
    sys.exit()