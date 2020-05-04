LARGURA = int(input("Digite a Largura: "))
ALTURA = int(input("Digite a Altura: "))


N1 = 0
N2 = 0

while N2 < ALTURA:
    while N1 < LARGURA:
        print("#", end = "")
        N1 =+ 1
    print()    
    N2 =+ 1
    N1 = 0
