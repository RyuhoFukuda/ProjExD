import pygame as pg
import sys
from random import randint

sky = True #空にいるかどうかを判定するグローバル変数

def collide(rct1, rct2, bird): #rct2がバード、rct1が足場
    global sky           
    if rct2.top < rct1.top and rct2.bottom < rct1.bottom and rct2.colliderect(rct1):
        rct2.bottom = rct1.top
        sky = False
    # if sky == False and rct2.centerx < rct1.left and rct2.colliderect(rct1):
    #     rct2.centerx = rct1.left
    # if sky == False and rct2.centerx > rct1.right and rct2.colliderect(rct1):
    #     rct2.centerx = rct1.right
    # elif sky == True and rct2.top > rct1.top and rct2.bottom > rct1.bottom and rct2.colliderect(rct1):
    #     rct2.centery = rct2.bottom+5
    #     bird.speed_y = 0

def draw_score(scr, time):
    fonto = pg.font.Font(None, 80)
    score = time // 1000
    txt = fonto.render(f"Score:{score}", True, "BLACK")
    scr.sfc.blit(txt, (10, 10))

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
        self.speed_y = 0
        self.jump_power = 0
        self.charge = False
    
    def blit(self, scr :Screen):
        return scr.sfc.blit(self.sfc, self.rct)

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
        
        pg.draw.rect(scr.sfc, (255, 0, 0), (self.rct.right, self.rct.centery, 20, 63))
        pg.draw.rect(scr.sfc, (255, 255, 255), (self.rct.right, self.rct.centery, 20, 63-self.jump_power*-5))

    #壁と天井の判定
    def wall_pass(self):
        if self.rct.right < 0:
            self.rct.left = 600
        if self.rct.left > 600:
            self.rct.right = 0
        if self.rct.top < 0:
            self.rct.top = 0

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
            

class FootFold:
    global sky
    def __init__(self, y, scr :Screen):
        self.sfc = pg.Surface((125, 10))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.rect(self.sfc,(255, 0, 0),(0, 0, 125, 10))
        self.rct = self.sfc.get_rect()
        self.y = y
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = self.y

    def blit(self, scr :Screen):
        return scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr :Screen):
        self.rct.centery += 1
        if self.rct.bottom > scr.rct.height:
            self.rct.centerx = randint(0, scr.rct.width)
            self.rct.bottom = 0
        self.blit(scr)


class Text:

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

def main():
    scr = Screen("飛べ！こうかとん", (600, 800), "ex06/aozora.jpg")
    bird = Bird("fig/1.png", 2.0, (300, 700))
    foot = FootFold(100, scr)
    foot1 = FootFold(300, scr)
    foot2 = FootFold(500, scr)
    foot3 = FootFold(700, scr)
    clock = pg.time.Clock()
    starttime = True

    while (1):
            
        scr.blit()
        bird.update(scr)
        foot.update(scr)
        foot1.update(scr)
        foot2.update(scr)
        foot3.update(scr)
        
        if starttime == True:
            first_box = pg.draw.rect(scr.sfc, (255,255,255), (250,780,100,10))
            collide(first_box, bird.rct, bird)
        collide(foot.rct, bird.rct, bird)
        collide(foot1.rct, bird.rct, bird)
        collide(foot2.rct, bird.rct, bird)
        collide(foot3.rct, bird.rct, bird)

        for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
                bird.jump(event)

        if bird.rct.top > scr.rct.height:
            break

        time = pg.time.get_ticks()
        draw_score(scr, time)
        pg.display.update() 
        clock.tick(120)
        if time >= 5000:
            starttime = False
        
    
    while (1):
        gmov = Text(f"Score:{str(time // 1000)}")
        gmov.update(scr)
        return

if __name__ == "__main__":
    pg.init() # 初期化
    main()
    pg.quit()
    sys.exit()