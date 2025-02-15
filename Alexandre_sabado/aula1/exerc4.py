# Conversor de temperatura

"""
Solicite ao Usuário para fornecer uma temperatura em Graus 
Converta essa temperatura em Fahrenheit
"""
print("Conversor de temperatura Fahrenheit")
print("Digite a temperatura em Celsius: ")
temp = float(input())

celsius = (temp * 1.8) + 32

print(f"Seu grau em Fahrenheit é: {celsius}°F ")


print("Conversor de temperatura Kelvin")
print("Digite a tempetura em Celsius: ")
tempK = float(input())

kelvin = tempK + 273.15

print(f"Seu graus em Kelvin é: {kelvin}K")