
def GetIn(cast, msg): # get user input
    while True:
        try:
            if (cast == None):
                return input(msg)
            else:
                return cast(input(msg))
        except ValueError:
            print("Valor inválido, por favor, tente novamente!")
        except (KeyboardInterrupt , EOFError): # ctrl+C or ctrl+d 
            Exit()
        

def ReturnMenu():
    GetIn(None, "Pressione Enter para voltar ao menu anterior") 

def Exit():
    print("\nObrigado por utilizar o algorítmo!")
    raise SystemExit

problems = { 1: " 1) Proprietário da empresa ABC LTDA...",
             2: " 2) Um dos sócios da empresa LYZ LTDA...",
             3: " 3) Lê o ano de nascimento...",
             4: " 4) Pedro comprou um saco de ração...",
             5: " 5) Ler dois valores para as variáveis A e B",
             6: " 6) Elaborar um programa que calcule...",
             7: " 7) Ler dois valores numéricos inteiros...",
             8: " 8) Preocupados com o valor do dólar...",
             9: " 9) [..] leia três valores numéricos inteiros",
            10: "10) Um aluno do BIA colocou uma esfera solida dentro de um aquário...",
            11: "11) Sair"
            }

def run():
    TxtInit = "\n Por favor, escolha um problema:\n"
    for p in problems:
        TxtInit +="     "+problems.get(p)+"\n"

    while True:
        problem = GetIn(int,TxtInit)


        if (problem == 1): # 1) Proprietário da empresa ABC LTDA
            salario = GetIn(float,"Informe o salário atual do funcionário: ")
            print("O novo sálario será ", (salario*1.25))
            ReturnMenu()


        elif (problem == 2): # 2) Um dos sócios da empresa LYZ LTDA...
            salario = GetIn(float,"Informe o salário atual do funcionário: ")
            percent = GetIn(float,"Informe o percentual a ser incrementado: ")
            print("O novo sálario será ", (salario*(1 + percent/100 )))
            ReturnMenu()



        elif (problem == 3): # Crie um programa que lê o ano de nascimento de uma pes....
            birth = GetIn(int,"Inoforme o ano de nascimento: ")
            this_year = GetIn(int, "Informe o ano atual: ")
            dif = this_year - birth
            
            # create dd/mm/yyy cast, datetime libray

            print("A diferença é ",dif," ano(s) ou")
            print(dif*12," meses ou")
            print(dif*12*30," dias ou ")
            print(dif*52," semanas")
            ReturnMenu()



        elif (problem ==4): # Pedro comprou um saco de ração com peso em quilo...
            food = GetIn(float,"Informe o peso do saco de ração em quilo: ")
            eat = GetIn(float, "Informe a quantidade diária de ração consumida em gramas: ")
            if (eat == 0):
                print("O consumo deve ser diferente de zero!")
                ReturnMenu()
                continue            
            food = food * 1000 # normalization
            food_days = food / eat
            if (food_days < 5):                
                print("Oh não! a ração vai acabar em ", food_days, " dias ")
            else:
                remaining = food - 5*eat
                print("Após o quinto dia restará ", remaining, " gramas de ração")
            ReturnMenu()



        elif (problem ==5): # 5) Ler dois valores para as variáveis A e B
            A = GetIn(None, "Informe o valor de A ")
            B = GetIn(None, "Informe o valor de B ")
            A, B = B, A 
            print("O valor de A é: ",A)
            print("O valor de B é: ",B)            
            ReturnMenu()            


        elif (problem ==6): # Elaborar um programa que calcule e apresente o valor do volume...
            print("Informe as dimensões da caixa:")
            compri = GetIn(float,"comprimento: ")
            Larg = GetIn(float,"Largura: ")
            altur = GetIn(float,"Altura: ")
            print("O voluem é ", Larg*compri*altur)
            ReturnMenu()            

        elif (problem ==7): # Ler dois valores numéricos inteiros
            A = GetIn(int, "Informe o valor de A ")
            B = GetIn(int, "Informe o valor de B ")
            print("O quadrado da diferença é: ", ((A-B)**2))
            ReturnMenu()

        elif (problem ==8): # Preocupados com o valor do dólar, uma importadora pede para os alunos
            print("a) Uma alterantiva é utilizar APIs e definir as necessidades da empresa, afinal se a manutenção está  em jogo, não seria preferível espelhar um servidor com os websocks da B3, nasdaq, Google Finanças?")
            dolar_hoje = GetIn(float,"Digite quanto está custando 1 dolar hoje: ") # dolar_hoje
            op = GetIn(float,"Informe o valor a ser convertido: ")

            print( op," reais é equivalente a ", op/dolar_hoje," dólares")
            print( op," dólares é equivalente a ", op*dolar_hoje," reais")


            # B
            GetIn(None, "Pressione Enter para ir para a B") 
            print("Uma sugestão seria usar a cadeia de markov, médias móveis, ..., mas qual a necessidade? precisamos tirar inferências?")
            dolar_ontem = GetIn(float,"De volta ao exercício, quanto estava custando 1 dolar ontem: ")

            if (dolar_ontem == 0):
                print("Desculpa! mas esse valor não pode ser computado")
                continue

            razao = dolar_hoje / dolar_ontem
            tag = " acréscimo " if (razao > 1) else " decréscimo "
            razao = abs((razao-1) * 100)
            print("Em relação a ontem, o dolar teve um",tag,"de ",razao,"%")
            ReturnMenu()        
        

        elif (problem ==9):
            name_var = ["A","B","C"]
            
            a = 0
            b = [0,0]
            for i in range(3):
                v = GetIn(int, "Informe a variável "+name_var[i]+": ")
                a+= v
                if (v**2 > b[0]):
                    b[0] = v**2
                    b[1] = i
                    
            print("O quadrado da soma é: ",a**2)
            print("O maior quadrado é da variável ",name_var[b[1]]," com valor ",b[0])
            ReturnMenu()

        elif (problem ==10):
            print("Considerando que o aquário está inicialmente cheio, as medidas em cm:")
            massa = (4/3)*3.1415*((25/2)**3)
            print("Sabemos que a massa da esfera é: ",massa," gramas, considerando g prox a 10 N/kg .:")
            print("O peso da esfera é: ", (massa/1000)*10," N") # massa precisa estar em kg para calcular a força peso

            ReturnMenu()
        elif (problem == 11): # exit
            Exit()



if __name__ == "__main__":
    run()

 
