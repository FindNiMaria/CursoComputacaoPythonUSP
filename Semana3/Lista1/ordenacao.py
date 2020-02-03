'''
Receba 3 números inteiros na entrada e imprima
crescente
se eles forem dados em ordem crescente. Caso contrário, imprima
não está em ordem crescente
'''

N1 = int(input("Insira o Primeiro Numero: "))
N2 = int(input("Insira o Segundo Numero: "))
N3 = int(input("Insira o Terceiro Numero: "))

if N1 < N2 and N2 < N3:
    print("Crescente")
else:
    print("Não está em ordem crescente")