import pygame as pg

#cores
clblack = (0,0,0)
clwhite = (255,255,255)

Objetos = []

class Tcontrol():
    def __init__(self):
        self.visible = True
        self.Enabled = True
        self.tag = 0
        self.caption = ""
        Objetos.append(self)

# Criar Classes para controlar a UAI
class Trect():
    """
        Interface responsavel por guardar as dimensoes dos objetos
    """
    def __init__(self,left,top,width = 0,heigth = 0):
        self.left = left
        self.top = top
        self.heigth = heigth
        self.width = width
    def rect(self):
        return [self.left,self.top, self.width,self.heigth]
    def size(self):
        return self.width,self.heigth
    def Inside(self,pos):
        return (self.left  > pos[0] > self.left+self.width) and (self.top > pos[1] > self.heigth+self.top)


class Tlabel():
    def __init__(self,txt,pos):
       self.txt = txt
       self.pos = pos 



class TButton( Tcontrol, Trect ):
    
    def __init__(self):
        Tcontrol.__init__(self)
        Trect.__init__(self,0, 0)
        
        # print( self.visible)




def start():

    pg.init()
    size  = width,heigth = 800,600
    screen = pg.display.set_mode(size=size)    

    b = TButton()
    b.left = 20
    b.top = 50
    b.width = 100
    b.heigth = 20
 
    print(Objetos[0].rect())

    while True:
        screen.fill((0,0,0))
        # Buscar os eventos do usuario
        for event in pg.event.get():
            if event.type == pg.QUIT: #Sai do jogo
                exit()
            elif event.type == pg.KEYUP:
                print(event)

            # <Event(1025-MouseButtonDown {'pos': (324, 200), 'button': 1, 'touch': False, 'window': None})>

        pg.draw.rect(screen,clwhite, b.rect() )
        pg.display.flip()





if __name__ == '__main__':
    start()