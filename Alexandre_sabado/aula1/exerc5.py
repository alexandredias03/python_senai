
# Numeros Pares em um intervalo

"""
Solicite dois números inteiros ao usuário
Representando o inicio e o fim de um intervalo
Mostre todos os numeros pares nesse intervalo
(incluindo limite inicial e final, se forem pares)
"""

print("Digite o primeiro número: ")
n1 = int(input())

print("Digite o segundo número: ")
n2 = int(input())

for y in range(n1, n2):
#    print(y)
   # if y != 0:
    if y % 2 == 0:
        print("o Numero é par", y)
        
