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
    """ 
        Classe responsável por controlar as opções basicas do Objeto 
    """
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
        self.SetRect(left,top,width,heigth)
        self.color = clwhite

    def SetRect(self, left,top,width,heigth):
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


class TEvent():
    """
        Classe responsavel por todos os eventos de mouse
    """
    def __init__(self):
        self.OnClick  = None        # dispara esse evento se clicar aqui
        self.OnMouseMove = None

    # Controla evento OnClick
    def Make_Click(self,posicao_clique):
        if (self.Inside(posicao_clique)) and (self.OnClick != None):
            self.OnClick(self)
            return True
        return False

    # Controla o Evento OnMouseMove
    def Make_Motion(self, posicao_motion):
        if (self.Inside(posicao_motion)) and (self.OnMouseMove != None):
            self.OnMouseMove(self)
            return True
        return False


class TButton( Tcontrol, Trect, TEvent):
    def __init__(self):
        self.color_font = clblack
        self.color = clwhite
        Tcontrol.__init__(self)
        Trect.__init__(self,0, 0)
        TEvent.__init__(self)
        
class Tlabel( Tcontrol,Trect, TEvent):
    def __init__(self,caption,pos):
        self.caption = caption
        Tcontrol.__init__(self)
        Trect.__init__(self, 0,0 )
        TEvent.__init__(self)


###################################################









def ClickButtonB(self):
    print("VC CLICOU NO BOTAO B")

def MouseMoveB(self):
    self.color = clred
    pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))


def MouseMoveFundo( ):
    Objetos[0].color = clwhite
    Objetos[1].color = clwhite
    pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
    

def clickC(self):
    print(self)

def moveC(self):
    self.color = (150,150,150)
    


def start():

    pg.init()
    size  = width,heigth = 800,600
    screen = pg.display.set_mode(size=size) 

    # incializa a fonte   
    font = pg.font.SysFont('courier new',30)
    #self.font = font.render(text,True,color)
    #self.rect = self.font.get_rect()

    # cria um botao
    b = TButton()
    b.SetRect(20, 50, 200, 200)
    b.OnClick =  ClickButtonB
    b.OnMouseMove =  MouseMoveB
    b.color = clwhite
    b.color_font = clblack
    b.caption = "123123"


    c = TButton()
    c.SetRect(200, 50, 200, 30)
    c.color = clwhite
    c.OnClick = clickC
    c.OnMouseMove = moveC
    c.visible = False

    
    L = Tlabel("123",(20,20) )
    L.color_font = clred


    #if isinstance(L,Tlabel):
    #    print("IS LABEL")
    

    while True:
        screen.fill((0,0,0))
        # Buscar os eventos do usuario
        for event in pg.event.get():
            if event.type == pg.QUIT: #Sai do jogo
                exit()

            elif event.type == pg.KEYUP:
                print(event)

            # vamos realizar o click em todos os objetos
            elif event.type == pg.MOUSEBUTTONDOWN: 
                for i in Objetos:
                    if i.visible:
                        if i.Make_Click(event.pos):
                            break

            elif event.type == pg.MOUSEMOTION: # Ao passar no Mouse
                backEvent = True
                for i in Objetos:
                    if i.visible:
                        if i.Make_Motion(event.pos):
                            backEvent = False
                            break
                if backEvent:
                    MouseMoveFundo()

            else:
                # print(event)
                pass

            # <Event(1025-MouseButtonDown {'pos': (324, 200), 'button': 1, 'touch': False, 'window': None})>



        #Desenha os objetos
        for obj in Objetos:
            if (obj.visible): 

                # Desenha os botoes
                if isinstance(obj,TButton):
                    #background
                    if obj.color != cltransparent:
                        pg.draw.rect(screen, obj.color , obj.rect() )

                    #Caption
                    text = font.render(obj.caption,True,obj.color_font)
                    screen.blit(text, (((obj.left+obj.width) - text.get_rect().width)//2,
                                       (((obj.top+obj.heigth) + text.get_rect().height)//2)
                                       ))
                
                #Desenha os Tlabels
                elif isinstance(obj,Tlabel):                        
                        text = font.render(obj.caption,True,obj.color_font)
                        screen.blit(text, (obj.left - (text.get_rect().width//2), obj.top - (text.get_rect().height//2)))

        pg.display.flip()





if __name__ == '__main__':
    start()