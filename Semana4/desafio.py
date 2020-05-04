NUMERO = input("Insira um numero inteiro..:  ")
TAMANHO = len(NUMERO)
print("O Número inserido tem", TAMANHO, "digitos")
NUMERO= int(NUMERO)
I = 1
SOMA = 0
DIVISOR = 10
while I <= TAMANHO:
    RESTO = NUMERO % 10
    SOMA = SOMA + RESTO
    print ("Somando", RESTO)
    NUMERO = int(NUMERO / 10)
    I = I + 1
    
print("O valor final da Soma é:", SOMA)