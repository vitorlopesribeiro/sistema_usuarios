from utils.manipulacao import adicionar_usuario, listar_usuarios, analisar_idade_media, buscar_por_profissao

usuarios = []
while True:
    print("\n=== Sistema de Cadastro de Usuários ===")
    print("1 - Adicionar novo usuário")
    print("2 - Listar todos os usuários")
    print("3 - Analisar média de idade")
    print("4 - Buscar por profissão")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        nome = input("Nome: ").strip().title()
        idade = int(input("Idade: "))
        profissao = input("Profissão: ").strip().lower()
        hobbies = input("Hobbies (separados por vírgula): ").split(",")
        hobbies = [h.strip().lower() for h in hobbies]
        usuario = adicionar_usuario(nome, idade, profissao, hobbies)
        usuarios.append(usuario)
        print(f"{nome} cadastrado com sucesso!")

    elif opcao == "2":
        listar_usuarios(usuarios)

    elif opcao == "3":
        media = analisar_idade_media(usuarios)
        print(f"Média de idade dos usuários: {media:.1f} anos")

    elif opcao == "4":
        prof = input("Digite a profissão para busca: ").strip().lower()
        encontrados = buscar_por_profissao(usuarios, prof)
        if encontrados:
            print("Usuários encontrados:")
            for u in encontrados:
                print(f"- {u['nome']} ({u['idade']} anos)")
        else:
            print("Nenhum usuário encontrado com essa profissão.")

    elif opcao == "5":
        print("Encerrando o sistema. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")
