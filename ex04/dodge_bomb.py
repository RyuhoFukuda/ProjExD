from tkinter import CENTER
import pygame as pg
import sys
from random import randint

def main():
    pg.init()
    #スクリーン作成
    pg.display.set_caption("逃げろ！こうかとん")
    w = 1400
    h = 700
    scrm_sfc = pg.display.set_mode((w, h))
    #背景　描画
    bg_sfc = pg.image.load("ex04\pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()
    #こうかとん　描画
    tori_sfc = pg.image.load("fig/tori.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 1050, 400
    tori_rct2 = tori_sfc.get_rect()
    tori_rct2.center = 350, 400
    #爆弾　描画
    bombx, bomby = randint(1, w), randint(1, h)
    bomb_sfc = pg.Surface((20, 20))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_sfc.set_colorkey("BLACK")
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.center = (bombx, bomby)
    bomb_rct2 = bomb_sfc.get_rect()
    bomb_rct2.center = (bombx, 0)
    #爆弾　速度
    vx = vy  = 2
    vy2 = 2

    #文字
    txt = "GAME OVER"
    fonts = []
    for size in range(8, 300):
        fonts.append(pg.font.Font(None, size))

    while(1):
        collapse = 0

        #反映
        bombx2 = randint(1, w)
        scrm_sfc.blit(bg_sfc, bg_rct)
        scrm_sfc.blit(tori_sfc, tori_rct)
        scrm_sfc.blit(tori_sfc, tori_rct2)
        scrm_sfc.blit(bomb_sfc, bomb_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        #こうかとんkeyイベント
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            tori_rct.move_ip(0, -1)
        if key_lst[pg.K_DOWN]:
            tori_rct.move_ip(0, 1)
        if key_lst[pg.K_LEFT]:
            tori_rct.move_ip(-1, 0)
        if key_lst[pg.K_RIGHT]:
            tori_rct.move_ip(1, 0)
        if key_lst[pg.K_q]:
            collapse = 1
        if key_lst[pg.K_w]:
            tori_rct2.move_ip(0, -1)
        if key_lst[pg.K_s]:
            tori_rct2.move_ip(0, 1)
        if key_lst[pg.K_a]:
            tori_rct2.move_ip(-1, 0)
        if key_lst[pg.K_d]:
            tori_rct2.move_ip(1, 0)


        
        #こうかとん壁判定
        if tori_rct.left < 0:
            tori_rct.left = 0
        if tori_rct.right > w:
            tori_rct.right = w
        if tori_rct.top < 0:
            tori_rct.top = 0
        if tori_rct.bottom > h:
            tori_rct.bottom = h

        if tori_rct2.left < 0:
            tori_rct2.left = 0
        if tori_rct2.right > w:
            tori_rct2.right = w
        if tori_rct2.top < 0:
            tori_rct2.top = 0
        if tori_rct2.bottom > h:
            tori_rct2.bottom = h
        
        #爆弾動き
        bomb_rct.move_ip(vx, vy)
        bomb_rct2.move_ip(0, vy2)
        #爆弾壁判定
        if bomb_rct.left < 0:
            vx *= -1
            vx *= 1.05
        if bomb_rct.right > w:
            vx *= -1
            vx *= 1.05
        if bomb_rct.top < 0:
            vy *= -1
            vy *= 1.05
        if bomb_rct.bottom > h:
            vy *= -1
            vy *= 1.05
        scrm_sfc.blit(bomb_sfc, bomb_rct2)
        if bomb_rct2.bottom > h:
            bomb_rct2.center = (bombx2, 0)
        #衝突判定
        if collapse == 0: #collapse変数が0のとき判定をONにする
            if tori_rct.colliderect(bomb_rct): 
                break
            if tori_rct2.colliderect(bomb_rct):
                break
            if tori_rct.colliderect(bomb_rct2):
                break
            if tori_rct2.colliderect(bomb_rct2):
                break
        elif collapse == 1: #collapse変数が1のとき判定をOFFにする
            pass
        pg.display.update()
        clock = pg.time.Clock()
        clock.tick(1000)

    #GAMEOVER画面
    while(1):
        for font in fonts:
            text = font.render(txt, True, (255,0,0))
            pos = font.size(txt)
            scrm_sfc.blit(bg_sfc, bg_rct)
            scrm_sfc.blit(text, (int((w-pos[0])/2),int((h-pos[1])/2)))
            pg.display.update()
            pg.time.wait(30)
            for event in pg.event.get():
                if event.type == pg.QUIT: return
    

if __name__ == "__main__":
    main()
    pg.quit()
    sys.exit()

