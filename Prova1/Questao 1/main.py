import pygame as pg


class Tobject():
    def __init__(self):
        self.visible = True
        self.enabled = True
        self.rect = 0,0,0,0

    def PosInside(self,pos):
        return (pos[0] >= rect[0]) and (pos[0] <= rect[0]+rect[2])


class Tbutton( Tobject ):
    def __init__(self, rect ):
        Tobject()    


def start():
    pg.init()
    size  = width,heigth = 800,600

    screen = pg.display.set_mode(size=size)    

    while True:

        # Buscar os eventos do usuario
        

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            elif event.type == pg.KEYUP:
                print(event)
            # <Event(1025-MouseButtonDown {'pos': (324, 200), 'button': 1, 'touch': False, 'window': None})>
            

        screen.fill((0,0,0))
        pg.display.flip()





if __name__ == '__main__':
    start()