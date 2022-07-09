import pygame as pg
from datetime import datetime
import random

#cores
clblack = (0,0,0)
clwhite = (255,255,255)
clred = (255,0,0)
cltransparent = (-1,-1,-1)
clbtnface =  (236, 233, 216)
# variavel para guardar todos os objetos
Objetos = {}
TEXTO_KEYBOARD = None





""" ###########################################################################################
    #                                                                                         #
    #                                 ORIENTAÇÃO  DE  OBJETOS                                 #
    #                                                                                         #
    ###########################################################################################"""

class Tcontrol():
    global Objetos
    """ 
        Classe responsável por controlar as opções basicas do Objeto 
    """
    def __init__(self,nome):
        self.visible = True
        self.Enabled = True
        self.tag = 0
        self.caption = ""
        self.color = clwhite
        self.color_font = clblack
        self.nome = nome
        Objetos[nome] = self



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
    def __init__(self, nome):
        Tcontrol.__init__(self,nome)
        Trect.__init__(self,0, 0)
        TEvent.__init__(self)
        
class Tlabel( Tcontrol,Trect, TEvent):
    """
        Classe para escrever palavras
    """
    def __init__(self,nome,caption,pos):

        Tcontrol.__init__(self,nome)
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
    UseSpace = False
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
        if len(TEXTO_KEYBOARD) > 0: #Apaga a ultima letra
            TEXTO_KEYBOARD = TEXTO_KEYBOARD[:-1]
            AfterKeyUP()
    # escreve a letra digitada
    elif len(evento.unicode) >0 and ((evento.unicode[0] in list('abcdefghijklmnopqrstuvwxyzçABCDEFGHIJKLMNOPQRSTUVWXYZÇ')) or ( (evento.key == 32) and (UseSpace) )):
        TEXTO_KEYBOARD += evento.unicode.upper()
        AfterKeyUP()
    elif evento.key ==  1073741903: # right
        pass
    elif evento.key ==  1073741904: # left
        pass
    elif evento.key ==  1073741905: # down
        pass
    elif evento.key ==  1073741906: # up
        pass
    else:
        print(evento)



""" ###########################################################################################
    #                                                                                         #
    #                          FIM DAS DECLARAÇÕES DE CLASSES                                 #
    #                                 Inicio da Engine                                        #
    #                                                                                         #
    ###########################################################################################"""

def MouseMoveFundo( ):
    """
        Ao mover o mouse pelo formulario
        **se nao encontrar nenhum componente
    """
    SetCursor(cr_arrow=True)
    Objetos['btt_insert'].color = clwhite
    Objetos['btt_screen_shot'].color = clwhite    
    Objetos['btt_show_words'].color = clwhite    
    
    


# funcao on Click do botao de salvar a imagem
SalvarImagem = False
def Btt_Screen_shot_Click(self,mouse_button):
    global SalvarImagem
    SalvarImagem = True
def ButtonMouseMove(self):
    self.color = clred
    SetCursor(cr_hand=True)



# ao clicar em uma letra da matriz
def OnClickLetra(self,mouse_button):
    print("Você clicou em um botao da matriz de letras (",self.x,'.',self.y,')')

# Evento apos soltar uma tecla
def AfterKeyUP():
    global TEXTO_KEYBOARD
    Objetos['Btt_Read'].caption = TEXTO_KEYBOARD   
   # Objetos['label'].caption = TEXTO_KEYBOARD





# "Alguns paragrafos do lorem ipsum"
Lorem_ipsum = "Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit amet consectetur adipisci velit, sed quia non numquam  eius modi tempora inci dunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur  At vero eos et accusamus et iusto odio dignissimos ducimus, qui blanditiis praesentium voluptatum deleniti atque corrupti, quos dolores et quas molestias excepturi sint, obcaecati cupiditate non provident, similique sunt in culpa, qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio, cumque nihil impedit, quo minus id, quod maxime placeat, facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet, ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. But I must explain to you how all this mistaken idea of reprobating pleasure and extolling pain arose. To do so, I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure  On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammeled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains."
# tratamento dos dados
Lorem_ipsum = Lorem_ipsum.replace(" ", "")
Lorem_ipsum = Lorem_ipsum.replace(",", "")
Lorem_ipsum = Lorem_ipsum.replace(".", "")
Lorem_ipsum = Lorem_ipsum.upper()

# inicia numa posicao aleatoria
Lorem_Start = random.randrange(len(Lorem_ipsum))
def GetLetra():
    """
        Funcao para gerar aleatoria uma letra
        cada letra da grade chama essa funcao
    """
    global Lorem_Start, Lorem_ipsum
    Lorem_Start+=1
    if Lorem_Start >= len(Lorem_ipsum):
        Lorem_Start = 0
    return Lorem_ipsum[Lorem_Start]


def Posicao_Valida(x,y, letra):
    """
        Verifica se a posicao X,Y pode ser usada para colocar uma letra
    """
    item = Objetos.get(str(x)+'.'+str(y))
    if item == None:
        return False
    else:
        if item.usado:
            if item.caption != letra:
                return False
        return True

def PreenchePosicao(x,y, letra):
    """
        Marca o objeto x,y com a letra!
    """
    item = Objetos.get(str(x)+'.'+str(y))
    if item == None:
        return False
    
    item.usado = True
    item.caption = letra

def Muda_Cor(x,y, cor):
    """
        Muda a cor de uma letra
    """
    item = Objetos.get(str(x)+'.'+str(y))
    if item == None:
        return False
    if item.usado:
        item.color = cor

def ClickButtonB(self,mouse_button):
    global TEXTO_KEYBOARD

    #Vamos procurar todos os lugares possiveis para adicionar a palavra
    # depois fazemos um choice
    # É força bruta? é! kkkkk qualquer coisa usamos a DGX para processar ahsduahsudas
    # A complexidade disso ficaria: 2(n)².(lg n).c, onde n é o numero de elementos da matriz, c é o tamanho da palavra
    # se são 25 * 40 = 1000 elementos, 1000² = 10^6 *c= 10^8. Ainda ta safe!
    if len(TEXTO_KEYBOARD) == 0:
        return 

    Posicoes_possiveis = [] # guardar todas as posicoes de insercao

    for xx in range(MapaConst['colunas']): 
        for yy in range(MapaConst['linhas']):
            pos_horizontal = True
            pos_vertical = True
            for c,letra in enumerate(TEXTO_KEYBOARD):
                if not Posicao_Valida(xx+c,yy,letra): # Ha uma posicao já utilizada aqui
                    pos_horizontal = False
                if not Posicao_Valida(xx,yy+c,letra): # Ha uma posicao já utilizada aqui
                    pos_vertical = False

            if pos_horizontal:
                Posicoes_possiveis.append( [xx,yy,0])
            if pos_vertical:
                Posicoes_possiveis.append( [xx,yy,1])
    
    if len(Posicoes_possiveis) > 0:
        p = random.choice(Posicoes_possiveis)
 
        for c,letra in enumerate(TEXTO_KEYBOARD):
            
            if p[2]: # coloca na posicao vertical
                PreenchePosicao(p[0],p[1]+c, TEXTO_KEYBOARD[c])
            else: # coloca na posicao horizontal
                PreenchePosicao(p[0]+c,p[1], TEXTO_KEYBOARD[c])

        TEXTO_KEYBOARD = ""
        AfterKeyUP() # atualiza
    else:
        print("Não há posições possiveis para inserir")


Mostrar_palavras = False
def btt_show_words_Click(self,mouse_button):
    """
        MUDA A COR DAS PALAVRAS ADICIONADAS
    """
    global Mostrar_palavras,MapaConst
    Mostrar_palavras = not Mostrar_palavras

    set_cor = clwhite
    if Mostrar_palavras:
         set_cor = clred

    #percorre todos os objetos
    for xx in range(MapaConst['colunas']): 
        for yy in range(MapaConst['linhas']):
            Muda_Cor(xx,yy,set_cor)





def MouseMoveB(self):
    self.color = clred
    SetCursor(cr_hand=True)
    


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


    






    
       


MapaConst = {}

TEXTO_KEYBOARD = ''

def start():
    global MapaConst, SalvarImagem

    pg.init()
    size  = width,heigth = 800,600
    screen = pg.display.set_mode(size=size) 

    # incializa a fonte   
    #font = pg.font.SysFont('courier new',20) # essa é minha fonte preferida, mas eu n sou o cliente kkk
    font = pg.font.SysFont('Times New Roman',16)
    
 

    # Vamos começar a criar os botoes:

    # armazena as configurações da matriz de letras
    MapaConst = {
        'borda': 20,
        'borda_top': 80,
        'borda_button': 50,

        'colunas': 40, # quantidade de letras nas colunas
        'linhas' : 25, # quantidade de letras nas linhas
    }
    # calcula o tamanho dos botoes de cada letra na matriz
    MapaConst['btt_width'] =(width - (2*MapaConst['borda'])) // MapaConst['colunas']
    MapaConst['btt_height'] = (heigth - MapaConst['borda_button'] - MapaConst['borda_top']) // MapaConst['linhas']


    Btt_Insert = TButton('btt_insert')
    Btt_Insert.SetRect( width - MapaConst['borda'] - 200, 20, 200, 40)
    Btt_Insert.caption = "Inserir Palavra"
    # eventos do botao
    Btt_Insert.OnClick =  ClickButtonB
    Btt_Insert.OnMouseMove =  MouseMoveB

    #Botao para pegar a palavra digitada pelo usuario
    Btt_Read = TButton('Btt_Read')
    Btt_Read.SetRect( MapaConst['borda'],20,200,40)
    Btt_Read.width = (width - (MapaConst['borda'] * 2)) - Btt_Insert.width

    Btt_Read.caption = ''
    Btt_Read.color = cltransparent
    Btt_Read.color_font = clred

    # Botao para Salvar a matriz de letras
    Btt_screen_shot = TButton('btt_screen_shot')
    Btt_screen_shot.SetRect( MapaConst['borda'], heigth - MapaConst['borda_button']+10, 200, 30)
    Btt_screen_shot.caption = 'Salvar Imagem'
    Btt_screen_shot.OnClick =  Btt_Screen_shot_Click # dispara esse evento quando clicar no botao
    Btt_screen_shot.OnMouseMove =  ButtonMouseMove # evento quando passa o mouse
    


    # Botao para Mostrar as Palavras Inseridas
    btt_show_words = TButton('btt_show_words')
    btt_show_words.SetRect( width - MapaConst['borda'] - 200, heigth - MapaConst['borda_button']+10, 200, 30)
    btt_show_words.caption = 'Mostrar Palavras'
    btt_show_words.OnClick =  btt_show_words_Click # dispara esse evento quando clicar no botao
    btt_show_words.OnMouseMove =  ButtonMouseMove # evento quando passa o mouse
    


    # label, texto informativo
    L = Tlabel('label',"Digite a palavra:",(0,0 ))
    L.color_font = clblack
    

    for y in range(MapaConst['linhas']):
        for x in range(MapaConst['colunas']):
                # cria um objeto Tbutton para cada letra
                btt_new_letra = TButton(str(x)+'.'+str(y))
                btt_new_letra.SetRect( MapaConst['borda'] + MapaConst['btt_width']*x,  
                                       MapaConst['borda_top'] + MapaConst['btt_height']*y,
                                       MapaConst['btt_width'], MapaConst['btt_height']
                                       )
                btt_new_letra.caption = GetLetra()
                btt_new_letra.x = x
                btt_new_letra.y = y
                btt_new_letra.OnClick = OnClickLetra
                btt_new_letra.usado = False



    ###########################################################################################
    #                                                                                         #
    #                                 Interface Gráfica                                       #
    #                                                                                         #
    ###########################################################################################

    t0 = datetime.now()
    desenha_cursor = True

    while True:

        """if (datetime.now() - t0) > 500:
            t0 = datetime.now()
            desenha_cursor = not desenha_cursor
        """
        screen.fill(clbtnface) # cor nostalgica do Delphi n poderia faltar!

        # Buscar os eventos do usuario
        for event in pg.event.get():
            if event.type == pg.QUIT: #Sai do jogo
                exit()

            elif event.type == pg.KEYUP:
                FormKeyUP(event)

            # vamos realizar o click em todos os objetos
            elif event.type == pg.MOUSEBUTTONDOWN: 
                for i in Objetos.values():
                    if i.visible:
                        if i.Make_Click(event.pos, event.button):
                            break

            elif event.type == pg.MOUSEMOTION: # Ao passar no Mouse
                backEvent = True
                for i in Objetos.values():
                    if i.visible:
                        if i.Make_Motion(event.pos):
                            backEvent = False
                            break
                if backEvent:
                    MouseMoveFundo()

            else:
                # print(event)
                pass



        #Desenha os objetos
        for obj in Objetos.values():
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

        # Salvar a Imagem?
        if  SalvarImagem:
            SalvarImagem = False
            # definir o rect apenas da matriz
            rect = pg.Rect(MapaConst['borda'], MapaConst['borda_top'], width - (MapaConst['borda']*2), heigth - MapaConst['borda_top'] - MapaConst['borda_button'])
            sub = screen.subsurface(rect)
            # salva
            pg.image.save(sub, "board.jpg")
            print("A imagem foi salva!")




if __name__ == '__main__':
    start()