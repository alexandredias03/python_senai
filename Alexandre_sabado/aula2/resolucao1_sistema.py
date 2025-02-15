# Criar novo arquivo
# Desenvolver um sistema que recebe 
# Valor de A, Valor de B e Valor de C
# Calcular a Bhaskara
# Delta = b² - 4 * a * c
# Bhaskara
"""
numA = float(input("Digite o valor A: "))
numB = float(input("Digite o valor B: "))
numC = float(input("Digite o valor C: "))

delta = (numB ** 2) - 4 * numA * numC # Ok

raizDelta = delta ** 0.5 # Ok

x1_p1 = -(numB)
x1_p2 = 2 * numA

x1 = (x1_p1 + raizDelta) / x1_p2


# print(delta)
# print(raizDelta)
# print(x1_p1)
# print(x1_p2)
print(x1)
"""
## RESOLUÇÃO PROF ARTHUR ////////////////////////////////////////////

import math 

print("Calculadora de Bhaskara")
a = float(input("Digite o valor de A"))
b = float(input("Digite o valor de B"))
c = float(input("Digite o valor de C"))

delta = b**2 - 4 * a * c
print("delta: ", delta)

raiz_delta = math.sqrt(delta) # Função de raiz

x1 = (-b + raiz_delta) / (2 * a)    
x2 = (-b - raiz_delta) / (2 * a)

print("O valor de x1 é:", x1)
print("O valor de x2 é:", x2)