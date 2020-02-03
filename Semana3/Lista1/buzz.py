'''
Exercícios 3 - FizzBuzz parcial, parte 2
Receba um número inteiro na entrada e imprima
Buzz
se o número for divisível por 5. Caso contrário, imprima 
o mesmo número que foi dado na entrada.
'''

N = int(input("Insira um Numero inteiro: "))

RESTO = N % 5

if RESTO == 0:
    print("Buzz")
else:
    print(N)