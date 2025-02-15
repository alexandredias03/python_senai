# Verificar se é impar ou par 

"""
Digite um numero inteiro 
Verifique se o numero é impar ou par 
Escreva a mensagem correspondente

"""

print("Verifique se o número é impar ou par")
print("Digite o numero:")
numero = int(input())

resto = numero % 2 # 10 / 2 = 0

if resto != 0:
    print("é um numero impar")
else:
    print("é um numero par")    