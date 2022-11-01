import pygame as pg
import sys
from random import randint


def check_bound(obj_rct, scr_rct): #壁判定
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


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
    
    key_delta = {
    pg.K_UP:    [0, -2],
    pg.K_DOWN:  [0, +2],
    pg.K_LEFT:  [-2, 0],
    pg.K_RIGHT: [+2, 0],
    }

    def __init__(self, bird_path, zup, default):
        self.sfc = pg.image.load(bird_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zup)
        self.rct = self.sfc.get_rect()
        self.rct.center = default[0], default[1]
    
    def blit(self, scr :Screen):
        return scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr :Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr)


class Bomb:

    def __init__(self, color, rad, var, scr :Screen):
        self.sfc = pg.Surface((20, 20)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, rad, 10) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = +var[0], +var[1]

    def blit(self, scr :Screen):
        return scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr :Screen):
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.rct.move_ip(self.vx, self.vy) 
        self.blit(scr)


class Sword:

    def __init__(self, zdwn, sword_path, bird :Bird):
        self.sfc = pg.image.load(sword_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zdwn)
        self.rct = self.sfc.get_rect()
        self.rct.center = bird.rct.centerx, bird.rct.top-self.rct.centery/2
    
    def blit(self, scr :Screen):
        return scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr :Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if self.rct.right < 0:
                    self.rct.right = 0
                if self.rct.left > scr.wh[0]:
                    self.rct.left = scr.wh[0]
                if self.rct.bottom < 0:
                    self.rct.bottom = 0
                if self.rct.top > scr.wh[1]:
                    self.rct.top = scr.wh[1]
        self.blit(scr)


class Gameover:

    def __init__(self, txt):
        self.txt = txt
        self.fonts = []
        for size in range(8, 300):
            self.fonts.append(pg.font.Font(None, size))

    def update(self, scr: Screen):
        for font in self.fonts:
            text = font.render(self.txt, True, (255,0,0))
            pos = font.size(self.txt)
            scr.blit()
            scr.sfc.blit(text, (int((scr.wh[0]-pos[0])/2),int((scr.wh[1]-pos[1])/2)))
            pg.display.update()
            pg.time.wait(30)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return


def main():

    pg.init() # 初期化
    scr = Screen("負けるな！こうかとん", (1200, 700), "ex05\pg_bg.jpg")
    bird = Bird("fig/1.png", 2.0, (600, 350))
    bomb = Bomb((0, 0, 255), (10, 10), (2, 2), scr)
    gmov = Gameover("GameOver")
    gmcr = Gameover("GameClear")
    sword = Sword(0.8, "fig/2.png", bird)
    gamemode = 0

    while (1):
        allive_flag = 0
        scr.blit()
        bird.update(scr)
        sword.update(scr)

        if sword.rct.colliderect(bomb.rct):
            allive_flag = 1
        if allive_flag == 0:
            bomb.update(scr)
            if bird.rct.colliderect(bomb.rct):
                break
        else:
            gamemode = 1
            break        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        pg.display.update() 
        clock = pg.time.Clock()
        clock.tick(1000)

    if gamemode == 0:
        while (1):
            gmov.update(scr)
            return
    else:
        while(1):
            gmcr.update(scr)
            return
        

if __name__ == "__main__":
    main()
    pg.quit()
    sys.exit()
