import pygame as pg

#cores
clblack = (0,0,0)
clwhite = (255,255,255)
clred = (255,0,0)
cltransparent = (-1,-1,-1)

# variavel para guardar todos os objetos
Objetos = []



###########################################
# Bora orientar a interface por objetos?  #

class Tcontrol():
    " Classe responsavel por controlar as opções basicas do Objeto "
    def __init__(self):
        self.visible = True
        self.Enabled = True
        self.tag = 0
        self.caption = ""
        Objetos.append(self)

class Trect():
    """
        Interface responsavel por guardar as dimensoes dos objetos
    """
    def __init__(self,left,top,width = 0,heigth = 0):
        self.left = left
        self.top = top
        self.heigth = heigth
        self.width = width
        self.color = clwhite

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
        self.OnClick  = None  # dispara esse evento se clicar aqui
        self.OnMouseMove = None

    def Make_Click(self,posicao_clique):
        if (self.Inside(posicao_clique)) and (self.OnClick != None):
            self.OnClick(self)
            return True
        return False

    def Make_Motion(self, posicao_motion):
        if (self.Inside(posicao_motion)) and (self.OnMouseMove != None):
            self.OnMouseMove(self)
            return True
        return False


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



def ClickButtonB(self):
    print("VC CLICOU NO BOTAO B")

def MouseMoveB(self):
    self.color = clred
    pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))


def MouseMoveFundo( ):
    Objetos[0].color = clwhite
    pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))

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
    b.OnMouseMove =  MouseMoveB
    b.color = clwhite

    
 


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
                    if i.Make_Click(event.pos):
                        break

            elif event.type == pg.MOUSEMOTION: # Ao passar no Mouse
                backEvent = True
                for i in Objetos:
                    if i.Make_Motion(event.pos):
                        backEvent = False
                        break
                if backEvent:
                    MouseMoveFundo()

            else:
                print(event)
                pass

            # <Event(1025-MouseButtonDown {'pos': (324, 200), 'button': 1, 'touch': False, 'window': None})>

        for obj in Objetos:
            # i.Make_Motion(event.pos)
            if obj.color != cltransparent:
                pg.draw.rect(screen, obj.color , obj.rect() )



        pg.display.flip()





if __name__ == '__main__':
    start()