'''
Receba um número inteiro na entrada e imprima
Fizz
se o número for divisível por 3. Caso contrário, imprima o mesmo 
número que foi dado na entrada.
'''

N = int(input("Insira um Numero inteiro: "))

RESTO = N % 3

if RESTO == 0:
    print("Fizz")
else:
    print(N) 