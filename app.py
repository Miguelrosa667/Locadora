from classes import Locadora, Cliente, Filme, Jogo

locadora = Locadora("CineGames", "Centro")

while True:
    print("\n===== MENU LOCADORA =====")
    print("1 - Cadastrar Cliente")
    print("2 - Cadastrar Filme")
    print("3 - Cadastrar Jogo")
    print("4 - Listar Itens")
    print("5 - Alugar Item")
    print("6 - Devolver Item")
    print("7 - Listar Itens de um Cliente")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    try:
        match opcao:
            case "1":
                nome = input("Nome do cliente: ")
                cpf = input("CPF do cliente: ")
                cliente = Cliente(nome, cpf)
                locadora.cadastrarCliente(cliente)

            case "2":
                codigo = int(input("Código do filme: "))
                titulo = input("Título do filme: ")
                genero = input("Gênero do filme: ")
                duracao = int(input("Duração em minutos: "))
                filme = Filme(codigo, titulo, genero, duracao)
                locadora.cadastrarItem(filme)

            case "3":
                codigo = int(input("Código do jogo: "))
                titulo = input("Título do jogo: ")
                plataforma = input("Plataforma: ")
                faixaEtaria = int(input("Faixa etária: "))
                jogo = Jogo(codigo, titulo, plataforma, faixaEtaria)
                locadora.cadastrarItem(jogo)

            case "4":
                locadora.listarItens()

            case "5":
                cpf = input("CPF do cliente: ")
                codigo = int(input("Código do item: "))
                cliente = locadora.buscar_cliente(cpf)
                item = locadora.buscar_item(codigo)
                if cliente and item:
                    cliente.locar(item)
                else:
                    print("Cliente ou item não encontrado.")

            case "6":
                cpf = input("CPF do cliente: ")
                codigo = int(input("Código do item: "))
                cliente = locadora.buscar_cliente(cpf)
                item = locadora.buscar_item(codigo)
                if cliente and item:
                    cliente.devolver(item)
                else:
                    print("Cliente ou item não encontrado.")

            case "7":
                cpf = input("CPF do cliente: ")
                cliente = locadora.buscar_cliente(cpf)
                if cliente:
                    cliente.listarItens()
                else:
                    print("Cliente não encontrado.")

            case "0":
                print("Saindo da locadora...")
                break

            case _:
                print("Opção inválida, tente novamente.")
    
    except Exception as e:
        print(f"Erro: {e}. Tente novamente.")
