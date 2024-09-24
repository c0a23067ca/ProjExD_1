import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_img_rct = kk_img.get_rect()
    kk_img_rct.center= 300,200
    
    tmr = 0
    while True:
        move_x=-1
        move_y=0
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            move_y+=-1
        if key_lst[pg.K_DOWN]:
            move_y+=1
        if key_lst[pg.K_RIGHT]:
            move_x+=2
        if key_lst[pg.K_LEFT]:
            move_x+=-1
        x=-(tmr%3200)
        kk_img_rct.move_ip((move_x,move_y))
        screen.blit(bg_img, [x, 0])
        screen.blit(pg.transform.flip(bg_img,True,False),[x+1600,0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(pg.transform.flip(bg_img,True,False),[x+4800,0])
        screen.blit(kk_img,kk_img_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()