from src.controller import produto_controller # type: ignore
from src.controller import usuario_controller

def exibir_menu():
    print("\nMAREA TOCA TUDO LTDA!")
    print("\n==== MENU ====")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produto")
    print("3 - Atualizar Produto")
    print("4 - Deletar Produto")
    print("5 - Buscar produto unico")
    print("6 - Cadastrar usuarios")
    print("7 - Listar usuário")
    print("0 - Sair")

def listar_produtos():
    print("\n --- Lista de Produtos --- ")  
    produtos = produto_controller.listar_produtos()  
    if produtos:
        for produto in produtos:
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preco: {produto['preco']}")
    else:
        print("Não existe produtos cadastrados")                

def cadastrar_produto():
    print("\n --- Cadastrar produto --- ")
    nome = input("Digite o nome: ")
    preco = input("Digite o preco: ")
    novo_id = produto_controller.cadastrar_produto(nome, preco)
    print(f"Produto cadastrado com sucesso com o novo ID {novo_id}.")    

def opcao_atualizar():
    print("\nATUALIZANDO O PRODUTO")
    produto_id = input("Digite o ID do produto: ")
    nome = input("Digite o nome do produto: ")
    preco = input("Digite o preco do produto: ")

    linhas = produto_controller.atualizar_produto(produto_id, nome, preco)
    if linhas > 0: # quantidade de linhas modificadas
        print("Produto atualizado com sucesso!")
    else:
        print("Nenhum produto foi atualizado")    

def listar_usuarios():
    print(" --- Listar usuarios --- ")
    usuarios = usuario_controller.listar_usuarios()
    if usuarios:
        for usuario in usuarios:
            print(f"ID {usuario['id']}, Usuário: {usuario['usuarioNome']}, E-mail: {usuario['email']}, Idade: {usuario['idade']}")    
    else:
        print("Não existe usuários cadastrados")        

def cadastrar_usuario():
    print(" --- Cadastrar usuarios --- ")
    usuarioNome = input("Digite seu usuário: ")
    email = input("Digite seu e-mail: ")
    idade = input("Digite sua idade: ")
    novo_id_usuario = usuario_controller.cadastrar_usuario(usuarioNome, email, idade)
    print(f"Usuário cadastrado com sucesso com novo ID {novo_id_usuario}.")

# main -> Inicializar o projeto
def main():
    # While True para repetir mesmo que a opção digitada esteja errada
    while True:

        exibir_menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_produto()
        elif opc == "2":
            listar_produtos()
        elif opc == "3":
            opcao_atualizar()    
        elif opc == "6":
            cadastrar_usuario()   
        elif opc == "7":
            listar_usuarios()     
        elif opc == "0":
            print("Saindo do sistema...")    
            # sys.exit(0)
        else:
            print("Opção Inválida, tente novamente...")                

if __name__=='__main__':
    main()