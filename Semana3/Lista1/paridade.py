'''
Receba um número inteiro na entrada e imprima
par
quando o número for par ou
ímpar
quando o número for ímpar.
'''

N = int(input("Insira um Valor: "))
RESTO = N % 2
if RESTO == 0:
    print("Par")
else:
    print("Impar")
