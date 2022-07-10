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

# Quando o usuario vai colocar o navio no tabuleiro
# essa variavel desenha o navio no mouse






""" ###########################################################################################
    #                                                                                         #
    #                                 ORIENTAÇÃO  DE  OBJETOS                                 #
    #                                                                                         #
    ###########################################################################################"""



class Tcontrol():
    global Objetos
    global state
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
        self.state = 0
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


class TPlayer():
    global MapaConst, Objetos

    def __init__(self):
        self.cor = clwhite
        self.cor_navio = clblack
        self.index = 0
        self.pontos = 0
        self.navios = [] # sequencia de elementos Tnavio

    def SetStatus(self):
        MapaConst['Form_color'] = self.cor
        Objetos['label_player'].caption = 'Jogador: '+str(self.index)

# Armazenar as informacoes de navio da Celula

class TNavio():
    def __init__(self, indice_player, _posicoes):        
        self.Posicoes = _posicoes
        self.player = GetPlayer(indice_player)
        self.player.navios.append(self)
        # marcar os elementos para fazerem referencia a esse navio
        for el in self.Posicoes:
            el.kind = self

    def Show_navio(self):
        for cell in self.Posicoes:
            cell.color = self.player.cor_navio

""" ###########################################################################################
    #                                                                                         #
    #                          FIM DAS DECLARAÇÕES DE CLASSES                                 #
    #                                 Inicio da Engine                                        #
    #                                                                                         #
    ###########################################################################################"""

 

# Evento apos soltar uma tecla
def AfterKeyUP():
    pass
   #global TEXTO_KEYBOARD
   # Objetos['Btt_Read'].caption = TEXTO_KEYBOARD   
   # Objetos['label'].caption = TEXTO_KEYBOARD


   


def GetAllSpaces():
    global Objetos
    """
        Essa funcao retorna todos os quadrados do jogo
    """
    for obj in Objetos.values():
        if hasattr(obj,'x') and hasattr(obj,'y'): # verifica se o objeto tem atributo x e y
            yield obj
        

def GetEspace(x,y):
    global Objetos
    return Objetos.get(str(x)+'.'+str(y))


def ChangeSpaceVisibility(player):
    """
         muda a visibilidade dos objetos pro jogador escolher a posicao para colocar o navio
    """
    for i in GetAllSpaces():
        i.visible = (i.choice_player == player)



def SelecionaRegioes():
    global MapaConst
    """
        Essa funcao retorna os possiveis quadrados para os jogadores escolherem
    """
    "-> cada item sorteado pode trazer 4 lugares"
    # se os valores totais sao multiplos de 4
    # de quantas formas podemos sortear 8 quadrantes de 16? o tempo exige outra abordagem:
    # 1- listar todos os quadrardos  4x4 disponiveis 

    # dividimos o mapa em blocos de 16 elementos
    qtd = MapaConst['colunas'] // 4, MapaConst['linhas']// 4

    combinacoes = []
    for x in range(qtd[0]):
        for y in range(qtd[1]):
            # adiciona todos os conjuntos diponiveis pro jogador colocar o navio
            combinacoes.append( (x,y) )
    
    # escolhe as combinacoes os jogadores

    for player in range(1,MapaConst['Num_players']+1): # EU PODERIA FAZER O JOGO COM 3 OU MAIS JOGADORES

        for jogador in range(5): # para cada jogador escolhe 4 posicoes no mapa para permitir que ele coloque o navio
            lugar = random.choice(combinacoes)
            combinacoes.remove(lugar)

            # marca o lugar nos objetos
            for x in range(4):
                for y in range(4):
                    GetEspace((lugar[0]*4)+x, (lugar[1]*4)+y).choice_player = player
                   

def ColocarNavio(self, dimensao, Horiontal):
    """
        FUNCAO PARA INSERIR UM NAVIO
    """

    # buscar as celulas que o navio impacta
    elementos = []
    for c in range(dimensao):
        if Horiontal:
            # se nao achar nessa posicao GetSpace retorna None
            elementos.append( GetEspace(self.x + c, self.y)) 
        else:
            elementos.append( GetEspace(self.x, self.y+c))

    # verificar se existe uma celula inválida
    if None in elementos:
        print("Lugar inválido para inserir um navio!")
        return
        
    #vamos buscar o indice do jogador
    player = GetPlayer()

    # verificar se o usuario pode inserir nesses lugares
    for el in elementos:
        if el.choice_player != player.index:
            print("Você não pode inserir nesse lugar!")
            return    

        # verificar se cada atributo Kind da celula está vazio ( se tiver um navio está referenciado aqui)
        if el.kind != None:
            print("Já existe um navio aqui!")
            return    

    Novo_Navio = TNavio(player.index,elementos)
    #mostra para o usuario
    Novo_Navio.Show_navio()

    # vamos colocar ele em cada celula
    # GetPlayer().
    # print(elementos)






def GetPlayer( indice = -1):
    """
        Funcao que retorna o jogador atual
    """
    global MapaConst
    for jogador in MapaConst['jogadores']:
        if indice == -1:
            if jogador.index ==  MapaConst['choice_player']:
                return jogador
        else:
            if jogador.index ==  indice:
                return jogador


    return None




""" ###########################################################################################
    #                                                                                         #
    #                              FUNCOES ONCLICK DOS OBJETOS                                #
    #                                                                                         #
    ###########################################################################################"""


def btt_next_player_click(self,mouse_button):
    """
        Funcao para o proximo jogador escolher as posicoes dos navios
    """ 
    global MapaConst
    MapaConst['choice_player'] += 1
    MapaConst['navio_orientacao']=True

    if MapaConst['choice_player'] > MapaConst['Num_players']:
        print("VAMOS INICIAR O JOGO")
    else:
        ChangeSpaceVisibility(MapaConst['choice_player'])
        GetPlayer().SetStatus() # atualiza o status do jogo para o proximo jogador

    MapaConst['Desenha_Navio'] = -1

    
    

def btt_muda_orientacao_click(self,mouse_button):
    """
       Funcao para mudar a orientação, quando o usuario vai colocar o navio no mapa
    """
    # orientacao vai ser salva na funcao mapa_const
    global MapaConst
    MapaConst['navio_orientacao'] = not MapaConst['navio_orientacao']
    


def btt_navio_click(self,mouse_button):
    """
        ao clicar no botao de adicionar navio

        guardar o estado de desenhar em uma variavel
    """
    global MapaConst
    MapaConst['Desenha_Navio'] = self.dimensao # variavel que permite desenhar o navio no mouse

    # MapaConst['navio_orientacao']
    pass


def ClickOcean(self,mouse_button):
    """
        EVENTO AO CLICAR NUMA POSICAO DO OCEANO
    """
    global MapaConst
    if (mouse_button == 1): # clicou com o botao esquerdo
        
        if MapaConst['Desenha_Navio'] > 0:
            ColocarNavio(self, MapaConst['Desenha_Navio'], MapaConst['navio_orientacao'])
            

    elif (mouse_button == 2): # clicou com o botao direito
        pass


def btt_play_Click(self,mouse_button):
    global state, MapaConst

    state = 2
    # seleciona os espacos possiveis para cada jogador
    SelecionaRegioes()

    
    MapaConst['choice_player'] = 1 # jogador 1 começa escolhendo a regiao do mapa
    ChangeSpaceVisibility(MapaConst['choice_player'])
    MapaConst['navio_orientacao'] = True

    # Criar os jogadores
    jogadores_qtd =  MapaConst['Num_players']
    MapaConst['jogadores'] = []
    for i in range(jogadores_qtd+1):
        player = TPlayer() # cria um novo jogador

        player.cor = (random.randrange(255),random.randrange(255),random.randrange(255))
        player.cor_navio = (random.randrange(255),random.randrange(255),random.randrange(255))
        
        player.index = i+1

        MapaConst['jogadores'].append (player) # adiciona o jogador num array
    
    GetPlayer().SetStatus()




""" ###########################################################################################
    #                                         ON MOVE                                         #
    ###########################################################################################"""

def ButtonMouseMove(self):
    global state
    self.color = clred
    SetCursor(cr_hand=True) 

def MouseMoveFundo( ):
    """
        Ao mover o mouse pelo formulario
        **se nao encontrar nenhum componente
    """
    SetCursor(cr_arrow=True)
    Objetos['btt_play'].color = clwhite
    Objetos['Next_player'].color = clwhite
    Objetos['change_orientation'].color = clwhite



def CriaObjetos():
    """
        Funcao para criar todas os objeto estruturas
    """
    global MapaConst, width,heigth, size
    # 1º botao para iniciar o jogo
    btt_play = TButton('btt_play')
    btt_play.SetRect( width - MapaConst['borda'] - 200, heigth - MapaConst['borda_button']+10, 200, 30)
    btt_play.caption = 'Iniciar o jogo'
    btt_play.OnClick =  btt_play_Click # dispara esse evento quando clicar no botao
    btt_play.OnMouseMove =  ButtonMouseMove # evento quando passa o mouse
    btt_play.state = 1 # cada tela tem um state

    btt_next_player = TButton('Next_player')
    btt_next_player.SetRect( width - MapaConst['borda'] - 200, heigth - MapaConst['borda_button']+10, 200, 30)
    btt_next_player.caption = 'Proximo Jogador'
    btt_next_player.OnClick =  btt_next_player_click # dispara esse evento quando clicar no botao
    btt_next_player.OnMouseMove =  ButtonMouseMove # evento quando passa o mouse
    btt_next_player.state = 2 # cada tela tem um state

    # botoes de navios
    navios = [2,3,3,4]
    for indice, navio in enumerate(navios):
        btt_nav = TButton('Navio.'+str(indice)+'.'+str(navio))

        # posicionar da esquerda para direita
        nav_width = (width  - (MapaConst['borda']*2)) // len(navios)

        btt_nav.SetRect( MapaConst['borda'] + (nav_width+2)*indice , MapaConst['borda_top']-40, nav_width, 30)

        btt_nav.dimensao = navio
        btt_nav.caption = 'Navio '+str(btt_nav.dimensao)
        btt_nav.OnClick =  btt_navio_click # dispara esse evento quando clicar no botao
        #btt_nav.OnMouseMove =  ButtonMouseMove # evento quando passa o mouse
        btt_nav.state = 2 # cada tela tem um state
        btt_nav.ref = [] # variavel responsavel por armazenar as posicoes dos navios

    

    ## BOTAO PARA MUDAR A ORIENTAÇÃO DE COLOCAR O NAVIO
    btt_muda_orientacao = TButton('change_orientation')
    btt_muda_orientacao.SetRect( MapaConst['borda'], heigth - MapaConst['borda_button']+10, 200, 30)
    btt_muda_orientacao.caption = 'Mudar a orientacao'
    btt_muda_orientacao.OnClick =  btt_muda_orientacao_click # dispara esse evento quando clicar no botao
    btt_muda_orientacao.OnMouseMove =  ButtonMouseMove # evento quando passa o mouse
    btt_muda_orientacao.state = 2 # cada tela tem um state


    # label jogador
    label_player = Tlabel('label_player',"Jogador: ",(MapaConst['borda'], 10 ))
    label_player.color_font = clblack
    label_player.state = 2


 

    ##CRIA OS SPACES  / OCEANO 
    for y in range(MapaConst['linhas']):
        for x in range(MapaConst['colunas']):
                # cria um objeto Tbutton para cada space
                btt_new_space = TButton(str(x)+'.'+str(y))
                btt_new_space.SetRect( MapaConst['borda'] + MapaConst['btt_width']*x,  
                                       MapaConst['borda_top'] + MapaConst['btt_height']*y,
                                       MapaConst['btt_width'], MapaConst['btt_height']
                                       )
                btt_new_space.caption = str(x)
                btt_new_space.x = x
                btt_new_space.y = y
                btt_new_space.OnClick = ClickOcean
                btt_new_space.usado = False
                btt_new_space.state = 2 # controla o desenho do componente, so quando o state global for igual
                btt_new_space.choice_player = 0 # essa propriedade vai permitir que os jogadores coloquem o navio
                btt_new_space.kind = None # tipo de elemento que tem na celula, pode ser um Tnavio ou ...


def EventsAnswer():
    """
        Funcao para tratar os evento
    """
    global Objetos, MapaConst

    # Buscar os eventos do usuario
    for event in pg.event.get():
        if event.type == pg.QUIT: #Sai do jogo
            exit()

        # vamos realizar o click em todos os objetos
        elif event.type == pg.MOUSEBUTTONDOWN: 
            for i in Objetos.values():
                if i.visible and state == i.state:
                    if i.Make_Click(event.pos, event.button):
                        break

        elif event.type == pg.MOUSEMOTION: # Ao passar no Mouse
            backEvent = True
            for i in Objetos.values():
                if i.visible and state == i.state:
                    if i.Make_Motion(event.pos):
                        backEvent = False
                        break
            if backEvent:
                MouseMoveFundo()

        else:
            # print(event)
            pass


""" ###########################################################################################
    #                                                                                         #
    #                                        START                                            #
    #                                                                                         #
    ###########################################################################################"""
    

def start():
    global state, MapaConst, size, width,heigth
    ## VAMOS CRIAR UM BATALHA NAVAL MAIS DIVERTIDO? ##
    # -> Os 2 jogadores vao usar o mesmo tabuleiro
    # -> Já que tem liberdade poética, vamos criar a minha versão!
    # 
    # -> Único problema... como fazer para os dois jogadores nao colocar navios no mesmo lugar?
    # -> O jogador so vai poder colocar um navio na regiao que o computador escolher
    # -> Como definir quantas regioes sao necessarias?
    # -> Depois nos pensamos kkkk
    # -> vamos codar um pouco
    #
    #
    #####################################################

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
        'borda_top': 100,
        'borda_button': 50,

        'colunas': 20, # quantidade de letras nas colunas
        'linhas' : 20, # quantidade de letras nas linhas

        'Num_players':2,
        'Desenha_Navio': -1, # tamanho do navio
        'navio_orientacao': True, # horizontal ou vertical

        'jogadores': [],  # armazenar todos os jogadores
        'Form_color': clwhite
    }


    # calcula o tamanho dos botoes de cada letra na matriz
    MapaConst['btt_width'] =(width - (2*MapaConst['borda'])) // MapaConst['colunas']
    MapaConst['btt_height'] = (heigth - MapaConst['borda_button'] - MapaConst['borda_top']) // MapaConst['linhas']

    # constroi os objetos
    CriaObjetos()     
    btt_play_Click(None,None)


    ###########################################################################################
    #                                                                                         #
    #                                 Interface Gráfica                                       #
    #                                                                                         #
    ###########################################################################################
    
    while True:
        # preenche a tela
        screen.fill(MapaConst['Form_color'])  

        #verifica os eventos, como click, on mousemove ...
        EventsAnswer() 



        #Desenha os objetos
        for obj in Objetos.values():
            if (obj.visible) and state == obj.state:

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

        ####################################
        # desenhar o navio seguind o mouse #
        ####################################
        if (MapaConst['Desenha_Navio'] > 0): #### PRINCIPAL VARIAVEL POR CONTROLAR O DESENHO
            mouse_pos = pg.mouse.get_pos()
            # se o mouse estiver dentro das posicoes
            if (MapaConst['borda'] < mouse_pos[0] < width - MapaConst['borda']) and (MapaConst['borda_top'] < mouse_pos[1]  < heigth - MapaConst['borda_button']):           
                    btt_width =  MapaConst['btt_width']
                    btt_height =  MapaConst['btt_height']
                    # adequa o rect ao tamanho do navio
                    if MapaConst['navio_orientacao']:
                        btt_width *= MapaConst['Desenha_Navio']
                    else:
                        btt_height *= MapaConst['Desenha_Navio']

                    # centralizar o navio do mouse na primeira celular
                    center_one = (MapaConst['btt_width'] // 2,  MapaConst['btt_height'] // 2)

                    pg.draw.rect(screen, GetPlayer().cor_navio , (mouse_pos[0] - center_one[0],
                                                    mouse_pos[1] - center_one[1], 
                                                    btt_width  ,
                                                    btt_height  ))
                                                    
            
               

        pg.display.flip()


#inicializa algumas variavei
MapaConst = {}
TEXTO_KEYBOARD = ''
state = 1 # cada componente tem um estado, se o estado for igual, então desenha


if __name__ == '__main__':
    start()





# 4 navios
# 8 areas
# 8 * 4 = 32

###################################
### vamos criar a BOMBA NUCLEAR ###
###################################
# uma posicao pode ter um rastreador
# uma posicao pode ter uma super bomba
# ganhar mais um tiro
# aleatoriamente as vezes pode cair uma bomba
# fica uma partida sem jogar





#Engine do jogo

# Start -> pinta o jogo


# -> 1º state = 1

# -> btt_play_click

# -> btt_next_player

