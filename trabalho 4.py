# Mensagem de boas-vindas
print("Bem-vindo a Livraria do Henrique")

# Lista vazia e variável id_global
lista_livro = []
id_global = 0

# Cadastrar livro
def cadastrar_livro(id):
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora: ")
    livro = {
        'id': id,
        'nome': nome,
        'autor': autor,
        'editora': editora
    }
    lista_livro.append(livro)
    print(f"Livro '{nome}' cadastrado com sucesso!")

# Consultar livro
def consultar_livro():
    while True:
        opcao = input("Consultar Livros: 1. Todos / 2. Por Id / 3. Por Autor / 4. Retornar ao menu: ")
        if opcao == '1':
            for livro in lista_livro:
                print(livro)
        elif opcao == '2':
            id_consulta = int(input("Digite o id do livro: "))
            livro_encontrado = next((livro for livro in lista_livro if livro['id'] == id_consulta), None)
            if livro_encontrado:
                print(livro_encontrado)
            else:
                print("Id inválido")
        elif opcao == '3':
            autor_consulta = input("Digite o nome do autor: ")
            livros_autor = [livro for livro in lista_livro if livro['autor'].lower() == autor_consulta.lower()]
            if livros_autor:
                for livro in livros_autor:
                    print(livro)
            else:
                print("Nenhum livro encontrado para este autor")
        elif opcao == '4':
            break
        else:
            print("Opção inválida")

# Remover livro
def remover_livro():
    while True:
        try:
            id_remover = int(input("Digite o id do livro a ser removido: "))
            livro_encontrado = next((livro for livro in lista_livro if livro['id'] == id_remover), None)
            if livro_encontrado:
                lista_livro.remove(livro_encontrado)
                print(f"Livro com id {id_remover} removido com sucesso!")
                break
            else:
                print("Id inválido")
        except ValueError:
            print("Por favor, digite um número válido")

# Menu Do código principal "Main"
while True:
    opcao = input("Menu: 1. Cadastrar Livro / 2. Consultar Livro / 3. Remover Livro / 4. Sair: ")
    if opcao == '1':
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == '2':
        consultar_livro()
    elif opcao == '3':
        remover_livro()
    elif opcao == '4':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida")

#
print("Cadastrando 3 livros de exemplo...")
id_global += 1
cadastrar_livro(id_global)  # Livro 1
id_global += 1
cadastrar_livro(id_global)  # Livro 2
id_global += 1
cadastrar_livro(id_global)  # Livro 3

# Consulta de todos os livros
print("Consultando todos os livros cadastrados:")
consultar_livro_opcao1 = input("Consultar Livros: 1. Todos / 2. Por Id / 3. Por Autor / 4. Retornar ao menu: ")
if consultar_livro_opcao1 == '1':
    for livro in lista_livro:
        print(livro)

# Consulta por código (id) de um dos livros
print("Consultando livro por ID (id 1):")
id_consulta = 1
livro_encontrado = next((livro for livro in lista_livro if livro['id'] == id_consulta), None)
if livro_encontrado:
    print(livro_encontrado)
else:
    print("Id inválido")

# Consulta por autor em que 2 livros sejam do mesmo autor
print("Consultando livros por autor (mesmo autor):")
autor_consulta = lista_livro[0]['autor']
livros_autor = [livro for livro in lista_livro if livro['autor'].lower() == autor_consulta.lower()]
if livros_autor:
    for livro in livros_autor:
        print(livro)
else:
    print("Nenhum livro encontrado para este autor")

# Remoção de um dos livros seguida de uma consulta de todos os livros
print("Removendo livro com id 1 e consultando todos os livros restantes:")
id_remover = 1
livro_encontrado = next((livro for livro in lista_livro if livro['id'] == id_remover), None)
if livro_encontrado:
    lista_livro.remove(livro_encontrado)
    print(f"Livro com id {id_remover} removido com sucesso!")
else:
    print("Id inválido")

print("Consultando todos os livros restantes:")
for livro in lista_livro:
    print(livro)
