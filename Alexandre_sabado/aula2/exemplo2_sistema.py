# Sistema de desconto de veiculos
# Solicite o nome do veiculo    
# E o preço do veiculo
# Se o preço > 80k -> 60% de desconto
# Se o preço > 50k -> 30% de desconto
# Se o preço < 30k -> Não existe desconto


"""

print("Bem-vindo a Senai Motors")

veiculo = (input("Qual seria o veiculo que deseja comprar: "))
preco = float(input("Preço: "))

percentual60 = 60
percentual30 = 30 

if preco >= 80000:
    desconto = preco - (preco * percentual60 / 100)
    print(f"O desconto do {veiculo} é de: {desconto} R$" )
elif preco >= 50000 <= 79999:
    desconto = preco - (preco * percentual30 / 100)
    print(f"O desconto do {veiculo} é de: {desconto} R$")
elif preco <= 49999:
    print(f"O {veiculo} não tem desconto!")


"""
#    Resolução prof Arthur ///////////////////////////////////////

nome_veiculo = input("Digite o nome do veiculo:")
preco_veiculo = float(input("Digite o preco do veiculo:"))

if preco_veiculo > 80000:
    desconto = 0.60
elif preco_veiculo > 50000:
    desconto = 0.30
else:
    desconto = 0

valor_desconto = preco_veiculo * desconto
valor_final = preco_veiculo - valor_desconto

print("Nome do veiculo é: ",valor_desconto)
print("O valor do veiculo é: ",valor_final)
print("O desconto foi: ",desconto)



