N = int(input("Digite um Número Inteiro: "))
SOMA = 0

while N != 0:
    S = N % 10
    SOMA  = SOMA + S
    N = N // 10

print(SOMA)