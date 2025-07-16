def adicionar_usuario(nome: str, idade: int, profissao: str, hobbies: list) -> dict:
    return {
        "nome": nome,
        "idade": idade,
        "profissao": profissao,
        "hobbies": list(set(hobbies))  # elimina duplicatas com conjunto
    }

def listar_usuarios(usuarios: list):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for i, u in enumerate(usuarios, start=1):
        print(f"\nUsuário {i}")
        print(f"Nome: {u['nome']}")
        print(f"Idade: {u['idade']}")
        print(f"Profissão: {u['profissao']}")
        print(f"Hobbies: {', '.join(u['hobbies'])}")

def analisar_idade_media(usuarios: list) -> float:
    if not usuarios:
        return 0.0
    idades = [u["idade"] for u in usuarios]  # list comprehension
    return sum(idades) / len(idades)

def buscar_por_profissao(usuarios: list, profissao: str) -> list:
    return [u for u in usuarios if u["profissao"] == profissao]
