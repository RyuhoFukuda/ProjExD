import pygame as pg
import sys
from random import randint

def main():
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
    tori_rct.center = 700, 250
    #爆弾　描画
    bombx, bomby = randint(0, w), randint(0, h)
    bomb_sfc = pg.Surface((20, 20))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_sfc.set_colorkey("BLACK")
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.center = (bombx, bomby)
    #爆弾　速度
    vx = vy= 1
    while(1):
        #反映
        scrm_sfc.blit(bg_sfc, bg_rct)
        scrm_sfc.blit(tori_sfc, tori_rct)
        scrm_sfc.blit(bomb_sfc, bomb_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT: return
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
        #こうかとん壁判定
        if tori_rct.left < 0:
            tori_rct.left = 0
        if tori_rct.right > w:
            tori_rct.right = w
        if tori_rct.top < 0: 
            tori_rct.top = 0
        if tori_rct.bottom > h:
            tori_rct.bottom = h
        #爆弾動き
        bomb_rct.move_ip(vx, vy)
        #爆弾壁判定
        if bomb_rct.left < 0:
            vx *= -1
        if bomb_rct.right > w:
            vx *= -1
        if bomb_rct.top < 0:
            vy *= -1
        if bomb_rct.bottom > h:
            vy *= -1
        #衝突判定
        if tori_rct.colliderect(bomb_rct): return
        
        pg.display.update()
        clock = pg.time.Clock()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init
    main()
    pg.quit()
    sys.exit()

