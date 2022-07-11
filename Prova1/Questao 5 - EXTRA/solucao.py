import numpy as np
from itertools import permutations
"""

"""
A = 0 # Qtd. de Arestas
N = 0 # Qtd. de Nós
B = 0 # Qtd. de Bananas
D = 0 # Indice do Nó que o Diddy está
Nos = [] # Nos[I] -> indice dos Nos que ligam a I
Bananas = [] # Bananas[i] == (Pi, Ei)  ->  Pi = indice do Node com a banana, Ei = Energia da banana
E = 0 # Energia Inicial do Donkey Kong

def ReadValues():
    """ LEITURA DOS INPUTS"""
    global A,N,B,D,Nos,Bananas,E
    A,N,B,E,D = [int(i) for i in input().split()]

    # Inicializa a matriz de Nós
    for n in range(N): 
        Nos.append( set() )
        
    for a in range(A):  # lê todas as arestas
        ai, aj = [int(i) for i in input().split()]
        Nos[ai].add(aj)
        Nos[aj].add(ai)

    #faz a leitura de todas as bananas
    for b in range(B): 
        Bananas.append( [int(i) for i in input().split() ])

def PrintRead(): 
    global A,N,B,D,Nos,Bananas,E
    """
        Print no array dos Nós e nas Bananas
    """
    print('Nos:', len(Nos))
    for i,n in enumerate(Nos):
        print(i,': ',n)

    print('Bananas:')
    for i,b in enumerate(Bananas):
        print(i,': ', list(b))


def Distance( NI, NF): 
    """
        pequeno DFS para buscar a distancia entre dois Nós
    """
    global N, _Distance_result
    cor = []
    _Distance_result = -1
    cor = [] # marcar os nós ja visitados
    for n in range(N): 
        cor.append(False)

    def dfs(pi, custo):
        global Nos, _Distance_result

        if (pi == NF):
            _Distance_result = custo

        if _Distance_result > -1: # já achou a distancia, então limpa a pilha
            return

        for i in Nos[pi]:
            if (cor[i] == False):
                cor[i] = True
                dfs( i, custo+1)  # empilha a funcao recursiva

    dfs(NI,0)
    return _Distance_result


"""
    Gerar uma combinação de todas as respostas possiveis
"""
ReadValues()


caminhos = [   ]
 
for indice, banana in enumerate(Bananas):
    for perm in permutations(Bananas,indice+1):
        caminhos.append(list(perm))

 
"""
    Calcular a distancia de todos os caminhos gerados
"""

buscas = [] # armazena as soluções

for caminho in caminhos: 
    caminho.append([D,0]) # adiciona o no do Diddy
    
caminhos.append([[D,0]]) # adiciona o menor caminho possivel



for caminho in caminhos:
    last_Element = 0 # comeca no nó zero
    temp_distancia = 0
    temp_energia = E
    Inserir = True
    for elemento in caminho:
        custo = Distance(last_Element, elemento[0])
        temp_distancia += custo
        temp_energia -= custo

        if temp_energia <= 0:
            Inserir = False
            break 

        temp_energia += elemento[1]
        last_Element = elemento[0]

    # vai inserir so se a energia nao zerar no caminho
    if Inserir:
        buscas.append( (temp_distancia, temp_energia) )
        #print( "NOVO CAMINHO:",caminho,"\n            distancia: ", temp_distancia,"  Energia ganha: ",temp_energia)



"""
    Imprimir o resultado
"""
if len(buscas) > 0: # se achou alguma solucao
    el = min(buscas, key= lambda x: x[0])
    print("A distância mínima percorrida pelo Donkey é:", el[0])
else:
    print("Donkey não consuigirá chegar!")


 