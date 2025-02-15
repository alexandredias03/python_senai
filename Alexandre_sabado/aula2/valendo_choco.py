# Verificar se uma palavra é um palindromo 
# Caso seja, exiba "É palindromo"
# Caso não seja, exiba "Não é um palindromo"
# A verificação deve ser Case Sensitive

# Valendo = barra de chocolate

## palindromo = input("Qual palavra é um palindromo? ")

palavra = input("Digite a palavra e verá se é palindromo ou não: ")

palavra = palavra.lower() ## strip // replace

if palavra == palavra[::-1]:
    print(palavra, "é um palindromo")
else:
    print(palavra, "não é um palindromo")

