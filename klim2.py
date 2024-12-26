import pygame as pg


#for i in range(9000, 11218):
#    if i % 5 != 0:
#        print(i, chr(i), end="\t")
#    else:
#        print(i, chr(i))
#print()


#symbs = {"0": chr(11035), "1": chr(9474), "2":chr(9552)}
#pole = [0 for _ in range(1, 83)]
#for i in range(1, len(pole)):
#    if i%9!=0:
#        print(symbs["1"]+symbs[str(pole[i])], end="")
#    else:
#        print(symbs["1"]+symbs[str(pole[i])]+symbs["1"])
#        print(symbs["2"]*30)
#print(chr(9600), chr(9604), chr(9209), chr(9609), chr(11035), chr(11036))


#PyGame!!!!!!!!


pg.init()
pg.mixer.init()
screen = pg.display.set_mode((729, 729))
pg.display.set_caption("Snake")
clock = pg.time.Clock()
run = True
FPS = 30
scale = [0, 0]
while run:
    screen.fill((0,0,0))
    key = pg.key.get_pressed()
    for e in pg.event.get():
        match e.type:
            case pg.QUIT:
                run = False
            
        if key[pg.K_UP]:
            if scale[1] < 2:
                scale[1] += 1
                scale[0] = 0
        if key[pg.K_DOWN]:
            if scale[1] > -2:
                scale[1] -= 1
                scale[0] = 0
        if key[pg.K_LEFT]:
            if scale[0] < 2:
                scale[0] += 1
                scale[1] = 0
        if key[pg.K_RIGHT]:
            if scale[0] > -2:
                scale[0] -= 1
                scale[1]=0

    for i in range(9):
        for j in range(9):
            cub_x = i *(27*(3-scale[0]+(i//3)*scale[0]))
            cub_y = j *(27*(3-scale[1]+(j//3)*scale[1]))
            if i % 2 == 0:
                if j % 2 == 0:
                    pg.draw.rect(screen, (255, 255, 255), (cub_x, cub_y, cub_x, cub_y))
                else:
                    pg.draw.rect(screen, (0, 0, 0), (cub_x, cub_y, cub_x, cub_y))
            else:
                if j % 2 != 0:
                    pg.draw.rect(screen, (255, 255, 255), (cub_x, cub_y, cub_x, cub_y))
                else:
                    pg.draw.rect(screen, (0, 0, 0), (cub_x, cub_y, cub_x, cub_y))
        
            
    clock.tick(FPS)
    pg.display.flip()
pg.quit()
