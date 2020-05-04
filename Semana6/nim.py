def computador_escolhe_jogada(n, m):
    num = n
    count = 0
    max = True
        
    while count < m:
        count = count + 1

        if (num - 1) % (m + 1) == 0:
            max = False
            jogadacomp = count
                
        num = num - 1

    if max:
        jogadacomp = m
           
    return jogadacomp

def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))
    while jogada > m or jogada <= 0:
        print("Jogada Invalida!")
        jogada = int(input("Quantas peças você vai tirar? "))
    
    return jogada

def partida(cont):
    n = int(input("Quantas Peças? "))
    m = int(input("Qual o maior número de peças a retirar? "))
    jogada = 0
    if n % (m + 1) == 0:
        print("Você começa! ")
        jogada = usuario_escolhe_jogada(n , m)
        n = n - jogada
        print("Você removeu", jogada, "peças")
        if n == 0:
            print("Fim de Jogo, Você ganhou! ")
        else:
            print("Restam", n, "Peças")
    else:
        print("Computador começa! ")
        
    while n > 0:
        if n > 0:
            jogada = computador_escolhe_jogada(n, m)
            n = n - jogada
            print("O Computador removeu", jogada, "peças")
            if n == 0:
                print("Fim de Jogo! O Computador Ganhou")
            else:
                print("Restam", n, "Peças")
        
            if n > 0:
                jogada = usuario_escolhe_jogada(n, m)
                n = n - jogada
                print("Você removeu", jogada, "peças")
                if n == 0:
                    print("Fim de Jogo, Você ganhou! ")
                else:
                    print("Restam", n, "Peças")
    cont = cont + 1
    return cont

def main():
    print("Bem vindo ao jogo do NIM! Escolha:  ")
    print("\n")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato 2")
    opcao = int(input())
    cont = 0
    if opcao == 1:
        print("Você escolheu uma partida isolada! ")
        while cont < 1:
            cont = partida(cont)
    elif  opcao == 2:
        print("Você escolheu um Campeonato! ")
        while cont < 3:
            print("Rodada", cont + 1)
            cont = partida(cont)
        
    else:
        print("Numero invalido! ")

main()