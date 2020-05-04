'''
Exercício 1
Escreva um programa que receba um número natural nn na entrada e imprima n! (fatorial) na saída.
Dica: lembre-se que o fatorial de 0 vale 1!
'''

N = int(input("Insira o Valor de N: "))
S = 1
while N > 0:
    if N == 0:
        S = 1
    else:
        S = S * N
        N = N - 1

print(S)