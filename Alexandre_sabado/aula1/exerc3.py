"""
Solicite o peso em kg e altura do usuario em metros
calcule IMC ( Indice de massa corporal )
peso / ( altura * altura )

exibir o IMC
"""

print("Verifique seu IMC")
print("Digite seu peso: ")
peso = float(input())

print("Digite sua altura: ")
altura = float(input())

resultado = peso / (altura * altura) 

print("Seu IMC é: ", resultado)






