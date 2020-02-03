'''
Exercício 1 - Distância entre dois pontos
Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente,
 às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, 
 às coordenadas x e y de um outro ponto no mesmo plano.
Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima
longe
na saída. Caso o contrário, quando a distância for menor que 10, imprima
perto
Dica: lembre-se que a fórmula da distância para dois pontos num plano cartesiano é a seguinte:
sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)
'''
import math

 X1 = float(input("Insira o Valor de X do ponto 1...: "))
​ Y1 = float(input("Insira o Valor de Y do ponto 1...: ")) 

 X2 = float(input("Insira o Valor de X do ponto 2...: "))
​ Y2 = float(input("Insira o Valor de Y do ponto 2...: ")) 

DISTANCIA = math.sqrt(((X1 - X2) ** 2) + ((Y1 - Y2) ** 2))

if DISTANCIA >= 10:
    print("Perto")
else:
    print("Longe")


    
'''
Exercício 2 - Desafio da videoaula
exercicio da aula com um porem:
Além disso, no caso de existirem 2 raízes reais, elas devem ser impressas em ordem crescente. Exemplos:
as raízes da equação são 1.0 e 2.0
as raízes da equação são -2.0 e 0.0
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
    if X1 > X2:
        print ("As raizes da equação são: ", X1,", ", X2)
        
    else:
        print ("As raizes da equação são: ", X2,", ", X1)

    