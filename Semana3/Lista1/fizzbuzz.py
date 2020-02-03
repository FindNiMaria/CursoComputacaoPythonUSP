'''
Receba um número inteiro na entrada e imprima
FizzBuzz
na saída se o número for divisível por 3 e por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.
'''

N = int(input("Insira um Numero inteiro: "))

RESTO3 = N % 3
RESTO5 = N % 5

if RESTO3 == 0 and RESTO5 == 0:
    print("FizzBuzz")
else:
    print(N)