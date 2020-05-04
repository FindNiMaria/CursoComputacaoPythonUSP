'''
Exercício 2
Receba um número inteiro positivo na entrada e imprima os nn primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.
'''

N = int(input("Insira um Valor: "))
NUM = 1
I = 1

while I <= N:
    if (NUM % 2) != 0:
        print(NUM)
        I = I + 1
        NUM = NUM + 1
    else:
        NUM = NUM + 1