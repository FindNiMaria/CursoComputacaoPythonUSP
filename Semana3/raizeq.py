'''
 se delta for igual a 0 so tem uma raiz
 se o delta for negativo nao existe raiz, mensagem de erro 
as raizes sao se for positivo maior q 0
'''

import math

A = int(input("Insira o Valor de A: "))
B = int(input("Insira o Valor de B: "))
C = int(input("Insira o Valor de C: "))

DELTA = B**2 * 4 * A * C

if DELTA < 0:
    print("Esta Equação Não possui raizes Reais")

else if DELTA == 0:
    X1 = -B + (math.sqrt(DELTA)) / (2 * A)
    print ("O resultado unico de X é: ", X1)

else if DELTA > 0:
    X1 = -B + (math.sqrt(DELTA)) / (2 * A)
    X2 = -B - (math.sqrt(DELTA)) / (2 * A)
    print ("x1 é igual a: ", X1)
    print ("x2 é igual a: ", X2)

