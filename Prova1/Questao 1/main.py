import pygame as pg

#cores
clblack = (0,0,0)
clwhite = (255,255,255)
clred = (255,0,0)
cltransparent = (-1,-1,-1)

# variavel para guardar todos os objetos
Objetos = []


TEXTO_KEYBOARD = None


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
        self.color = clwhite
        self.color_font = clblack
        Objetos.append(self)



class Trect():
    """
        Interface responsavel por guardar as dimensoes dos objetos
    """
    def __init__(self,left,top,width = 0,heigth = 0):
        self.SetRect(left,top,width,heigth)
 

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
    def Make_Click(self,posicao_clique, mouse_button):
        if (self.Inside(posicao_clique)) and (self.OnClick != None):
            self.OnClick(self,mouse_button)
            return True
        return False

    # Controla o Evento OnMouseMove
    def Make_Motion(self, posicao_motion):
        if (self.Inside(posicao_motion)) and (self.OnMouseMove != None):
            self.OnMouseMove(self)
            return True
        return False


# Vamos criar as Classes finais:
class TButton( Tcontrol, Trect, TEvent):
    """
        Classe Estilo um Botao, receber clicks
    """
    def __init__(self):
        Tcontrol.__init__(self)
        Trect.__init__(self,0, 0)
        TEvent.__init__(self)
        
class Tlabel( Tcontrol,Trect, TEvent):
    """
        Classe para escrever palavras
    """
    def __init__(self,caption,pos):

        Tcontrol.__init__(self)
        Trect.__init__(self, 0,0 )
        TEvent.__init__(self)
        self.caption = caption
        self.SetRect( pos[0],pos[1],0,0)





###################################################



def SetCursor(cr_arrow = False, cr_hand = False):
    if cr_arrow:
        pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
    elif cr_hand:
        pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))


def FormKeyUP( evento ):    
    UseSpace = True
    """
        Solucionar a escrita  poderia trazer bastante linhas de códigos, 
        pq uma abordagem comum é buscar o elemento com foco e modificar o texto.
        Aqui, como um tradeOff, vamos inverter!
            Vamos usar um ponteiro global (ops o python n tem essas coisas hahaha),
            brincadeiras a parte, vamos usar um buffer global e escrever sobre essa variavel
    """
    global TEXTO_KEYBOARD

    if evento.key == 13: 
        #funcoes com o enter, poderiam ser aproveitadas aqui
        return
    elif evento.key == 27:
        # funcoes com o ESC
        return



    if TEXTO_KEYBOARD == None:
        return

    if evento.key == 8: # backspace
        if len(TEXTO_KEYBOARD) > 0:
            #Apaga a ultima letra
            TEXTO_KEYBOARD = TEXTO_KEYBOARD[:-1]
            AfterKeyUP()

    elif len(evento.unicode) >0 and ((evento.unicode[0] in list('abcdefghijklmnopqrstuvwxyzçABCDEFGHIJKLMNOPQRSTUVWXYZÇ')) or ( (evento.key == 32) and (UseSpace) )):
        TEXTO_KEYBOARD += evento.unicode.upper()
        AfterKeyUP()
    else:
        print(evento)








def ClickButtonB(self,mouse_button):
    print("VC CLICOU NO BOTAO B,  button:", mouse_button)

def MouseMoveB(self):
    self.color = clred
    SetCursor(cr_hand=True)
    


def MouseMoveFundo( ):
    Objetos[0].color = clwhite
    Objetos[1].color = cltransparent
    Objetos[1].color_font = clwhite
    SetCursor(cr_arrow=True)
    


def moveC(self):
    # self.color = (150,150,150)
    self.color_font = clred
    SetCursor(cr_hand=True)



def clickC(self,mouse_button):
    global TEXTO_KEYBOARD
    
    if (TEXTO_KEYBOARD == None):
        TEXTO_KEYBOARD = ""
    else:
        TEXTO_KEYBOARD = None



def AfterKeyUP():
    global TEXTO_KEYBOARD
    print("Estou aqui!")
    Objetos[1].caption = TEXTO_KEYBOARD




def start():

    pg.init()
    size  = width,heigth = 800,600
    screen = pg.display.set_mode(size=size) 

    # incializa a fonte   
    font = pg.font.SysFont('courier new',30)
 
    # cria um botao
    b = TButton()
    b.SetRect(20, 50, 200, 200)
    b.OnClick =  ClickButtonB
    b.OnMouseMove =  MouseMoveB
    b.caption = "123123"


    c = TButton()
    c.SetRect(450, 50, 200, 30)
    c.color = cltransparent
    c.OnClick = clickC
    c.OnMouseMove = moveC
    c.visible = True
    c.caption = 'Palavras'
    c.color_font = clred
    
    L = Tlabel("Palavras",(478,100 ))
    L.color_font = clred

 
    

    while True:
        screen.fill((0,0,0))
        # Buscar os eventos do usuario
        for event in pg.event.get():
            if event.type == pg.QUIT: #Sai do jogo
                exit()

            elif event.type == pg.KEYUP:
                FormKeyUP(event)

            # vamos realizar o click em todos os objetos
            elif event.type == pg.MOUSEBUTTONDOWN: 
                for i in Objetos:
                    if i.visible:
                        if i.Make_Click(event.pos, event.button):
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
                    screen.blit(text, (   ( obj.left+ ((obj.width - text.get_rect().width)//2 ) ),
                                          ( obj.top+ ((obj.heigth - text.get_rect().height)//2) )
                                ))
  
                
                #Desenha os Tlabels
                elif isinstance(obj,Tlabel):      
                    text = font.render(obj.caption,True,obj.color_font)
                    screen.blit(text, (obj.left , obj.top ))


        pg.display.flip()


if __name__ == '__main__':
    start()