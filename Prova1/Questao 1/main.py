import pygame as pg

#cores
clblack = (0,0,0)
clwhite = (255,255,255)

# variavel para guardar todos os objetos
Objetos = []



###########################################
# Bora orientar a interface por objetos?  #

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
        return (self.left  < pos[0] < self.left+self.width) and (self.top < pos[1] < self.heigth+self.top)


class TMouseEvent():
    """
        Classe responsavel por todos os eventos de mouse
    """
    def __init__(self):
        self.OnClick = None

    def Make_Click(self,posicao_clique):
        if (self.Inside(posicao_clique)) and (self.OnClick != None):
            self.OnClick()


class Tlabel():
    def __init__(self,txt,pos):
       self.txt = txt
       self.pos = pos 



class TButton( Tcontrol, Trect, TMouseEvent):
    
    def __init__(self):
        Tcontrol.__init__(self)
        Trect.__init__(self,0, 0)
        TMouseEvent.__init__(self)
        # print( self.visible)



def ClickButtonB():
    print("VC CLICOU NO BOTAO B")



def start():

    pg.init()
    size  = width,heigth = 800,600
    screen = pg.display.set_mode(size=size)    

    b = TButton()
    b.left = 20
    b.top = 50
    b.width = 100
    b.heigth = 20
    b.OnClick =  ClickButtonB

 
    print("OBJETOS: ",len(Objetos))

    while True:
        screen.fill((0,0,0))
        # Buscar os eventos do usuario
        for event in pg.event.get():
            if event.type == pg.QUIT: #Sai do jogo
                exit()
            elif event.type == pg.KEYUP:
                print(event)
            elif event.type == pg.MOUSEBUTTONDOWN: # vamos realizar o click em todos os objetos
                
                for i in Objetos:
                    i.Make_Click(event.pos)

                print(event)
            else:
                #print(event)
                pass

            # <Event(1025-MouseButtonDown {'pos': (324, 200), 'button': 1, 'touch': False, 'window': None})>

        pg.draw.rect(screen,clwhite, b.rect() )
        pg.display.flip()





if __name__ == '__main__':
    start()