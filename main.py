import pygame as pg
import time
from math import sqrt
from PIL import Image
pg.init()
DISPLAY_HEIGHT = 480
DISPLAY_WIDTH = 945
screen = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pg.display.update()
screen.fill((255,255,255))
menu_image = pg.image.load('для пейнта меню.png')
menu_rect = (0,0,97,945)
pryamoug=None
kist = None
liniya = None
krug = None
krug_nach = None
pryamoug_nach = None
liniya_nach = None
zalivka = 0
cherniy,seriy,bordoviy,crasniy,orange,yellow,zeleniy,goluboy,siniy,beliy=[(0,0,0),(192,192,192),(58,6,3),(235,51,36),(240,155,89),(255,253,85),(117,249,77),(0,162,232),(63,72,204),(255,255,255)]
color = cherniy
while True:
    x_mouse, y_mouse = pg.mouse.get_pos()# получаем корды мыши
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type == pg.KEYDOWN:                      # если нажать ESK очистится все что нарисовано
            if event.key == pg.K_ESCAPE:
                screen.fill((255, 255, 255))
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == pg.BUTTON_LEFT:
                if 90<x_mouse<125 and 0<y_mouse<35:         # тут в условиях при нажатии на ЛКМ координаты курсора должны быть
                    pryamoug = True                         # в пределах некоторых чтобы включались определенный функции
                    kist = None                     #соответственно прямоугольник, круг, линия и кисть не могут быть включены одновременно
                    liniya = None
                    krug = None
                elif 0<x_mouse<39 and 0<y_mouse<36:
                    kist = True
                    pryamoug = None
                    liniya = None
                    krug = None
                elif 45 <x_mouse<82 and 0 < y_mouse<36:
                    liniya = True
                    pryamoug = None
                    kist = None
                    krug = None
                elif 131<x_mouse<167 and 0<y_mouse<36:
                    krug = True
                    pryamoug = None
                    kist = None
                    liniya = None
                elif 190<x_mouse<472 and 0<y_mouse<50:                  #когда заливка = 0 то фигура строится сплошной
                    zalivka = 5                                         #когда заливка = 5 то фигура строится со стенками в 5 пикселей
                elif 190 < x_mouse < 472 and 50 <= y_mouse < 97:
                    zalivka = 0
                elif 560 < x_mouse < 590 and 0 < y_mouse < 40:          #цвет просто перезаписывается в переменную(все цвета вначале объявлены)
                    color = cherniy
                elif 590 < x_mouse < 616 and 0 < y_mouse < 40:
                    color = seriy
                elif 616 < x_mouse < 645 and 0 < y_mouse < 40:
                    color = bordoviy
                elif 645 < x_mouse < 676 and 0 < y_mouse < 40:
                    color = crasniy
                elif 676 < x_mouse < 706 and 0 < y_mouse < 40:
                    color = orange
                elif 706 < x_mouse < 736 and 0 < y_mouse < 40:
                    color = yellow
                elif 736 < x_mouse < 766 and 0 < y_mouse < 40:
                    color = zeleniy
                elif 766 < x_mouse < 796 and 0 < y_mouse < 40:
                    color = goluboy
                elif 796 < x_mouse < 826 and 0 < y_mouse < 40:
                    color = siniy
                elif 826 < x_mouse < 860 and 0 < y_mouse < 40:
                    color = beliy
                elif 905 < x_mouse < 945 and 0 < y_mouse < 38:                          #чтоб сохранить рисунок сначала сохраняю всю область
                    pg.image.save(screen, 'pictures.png')                               # затем при помощи библиотеки PIL открываю рисунок со всей областью
                    im = Image.open('pictures.png')
                    im_crop = im.crop((0, 100, DISPLAY_WIDTH, DISPLAY_HEIGHT))           #вырезаю меню из неё меню и пересохраняю
                    im_crop.save('pictures.png')
            if pryamoug is True and pryamoug_nach is not True and y_mouse>97:       #если нажата кнопка для рисования прямоугольника, и курсор имеет корду по y>97 и при этом корды начальной точки прямоугольника не зареганы
                x_rect_nach,y_rect_nach = pg.mouse.get_pos()                        #сохраняем начальной точки прямоугольника
                pryamoug_nach = True                                                #корды объявили
            elif krug is True and y_mouse>97:                                       # с кругом и линией +- также
                x_krug_nach,y_krug_nach = pg.mouse.get_pos()
                krug_nach = True
            elif liniya is True and y_mouse>97:
                x_liniya_nach, y_liniya_nach = pg.mouse.get_pos()
                liniya_nach = True
        elif kist is True and y_mouse>97 and pg.mouse.get_pressed()[0] is True:     #если кисть активирована и корда по y>97 и левая кнопка мыши зажата
            pg.draw.circle(screen,color,(x_mouse,y_mouse),5)                        # много раз рисуется круг с радиусом 5
        elif event.type == pg.MOUSEBUTTONUP:
            if pryamoug_nach is True and pryamoug is True and y_mouse>97:
                x_rect_kon, y_rect_kon = pg.mouse.get_pos()
                if x_rect_nach <= x_rect_kon and y_rect_nach <= y_rect_kon:     #тут чистая матеша(прямоугольник в пайгейме рисуется из левой верхней точки в правую нижнюю, поэтому тут просто разные случаи рассмотрены)
                    pg.draw.rect(screen, color, (x_rect_nach, y_rect_nach, x_rect_kon-x_rect_nach, y_rect_kon-y_rect_nach),zalivka)
                elif x_rect_nach<x_rect_kon and y_rect_nach > y_rect_kon:
                    pg.draw.rect(screen, color,(x_rect_nach, y_rect_kon, x_rect_kon - x_rect_nach, y_rect_nach - y_rect_kon),zalivka)
                elif x_rect_nach > x_rect_kon and y_rect_nach <= y_rect_kon:
                    pg.draw.rect(screen, color,(x_rect_kon, y_rect_nach, x_rect_nach - x_rect_kon, y_rect_kon - y_rect_nach),zalivka)
                elif x_rect_nach > x_rect_kon and y_rect_nach > y_rect_kon:
                    pg.draw.rect(screen, color,(x_rect_kon, y_rect_kon, x_rect_nach - x_rect_kon, y_rect_nach - y_rect_kon),zalivka)
                pryamoug_nach = None
            elif krug_nach is True and krug is True and y_mouse>97:
                x_krug_kon,y_krug_kon = pg.mouse.get_pos()
                pg.draw.circle(screen, color, (x_krug_nach, y_krug_nach), sqrt(pow(x_krug_nach - x_krug_kon,2)+pow(y_krug_nach-y_krug_kon,2)),zalivka)   #радиус круга тоже вычисляем как в матеше по координатам
                krug_nach = None
            elif liniya_nach is True and liniya is True and y_mouse>97:
                x_liniya_kon, y_liniya_kon = pg.mouse.get_pos()
                pg.draw.line(screen, color, (x_liniya_nach,y_liniya_nach), (x_liniya_kon,y_liniya_kon), 5)
                liniya_nach=None
    screen.blit(menu_image, menu_rect)                      #поверх все время рисуется меню, граница меню и какой сейчас цвет активный
    pg.draw.circle(screen, color, (517, 30), 20)
    pg.draw.line(screen, cherniy, (0, 97), (945, 97), 5)
    pg.display.flip()