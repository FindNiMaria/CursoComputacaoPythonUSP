LARGURA = int(input("Digite a Largura: "))
ALTURA = int(input("Digite a Altura: "))


N1 = 1
N2 = 1

while N2 <= ALTURA:
    if N2 == 1 or N2 == ALTURA:
        while N1 <= LARGURA:
            print("#", end = "")
            N1 += 1
        print()    
        N2 += 1
        N1 = 1
    else:
        while N1 <= LARGURA:
            if N1 == 1:
                print("#", end = "")
            
            elif N1 == LARGURA:
                print("#")
                
            else:
                print(" ", end = "")
            N1 += 1    
        N2 += 1
        N1 = 1