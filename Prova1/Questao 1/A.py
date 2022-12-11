def main():
    s = "programacao"
    f = "aprovado"
    c = input('Entre com a letra para a alocação:')
    
    # quantas letras existem e em que posições?
    lst = []
    
    for pos,char in enumerate(s):
        if(char == c):
            lst.append(pos)
           
    print("posições onde foi encontrada a letra 'a'",lst)

    lposi = lst[1]
    x = 0
    for l in s:
        if x == lposi:
            print(f)
        else:
            print(l)
    x+=1

main()

#### EXEPLICAÇÃO
"""  
 O laço "for" da linha 9 procura os caracteres iguais aos que o usuario digitou ( armazenado na variavel c) e
 armazena a posicao desses caracteres numa lista.

 A ideia principal desse algorimo é tentar achar indices e fixar outras palavras.
 nesse caso, uma dessas tentativas iniciais está armazena em X

 Por fim, nesse exemplo, também concluimos que o algorítmo tem uma complexidade linear, 
 isto é, O(N), onde N é o tamamanho da string s.

 """