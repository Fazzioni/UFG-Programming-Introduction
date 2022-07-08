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
        Bananas.append( int(i) for i in input().split() )

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
for b in Bananas:
    print(b)

#print(    Distance(0,D)  )




