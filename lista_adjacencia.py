grafo = {}


def inserir_vertice(v):
    if v == "":
        print("Nome invalido")
        return
    if " " in v:
        print("O nome do vertice nao pode ter espaco")
        return
    if v in grafo:
        print("O vertice", v, "ja existe")
        return
    grafo[v] = []
    print("Vertice", v, "inserido")


def remover_vertice(v):
    if v not in grafo:
        print("Vertice nao encontrado")
        return
    del grafo[v]
    print("Vertice", v, "removido")


def mostrar_grafo():
    if len(grafo) == 0:
        print("Grafo vazio")
        return
    for v in grafo:
        print(v, "->", ", ".join(grafo[v]))


def menu():
    print()
    print("------ GRAFO (Lista de Adjacencia) ------")
    print("1 - Inserir vertice")
    print("2 - Remover vertice")
    print("9 - Mostrar grafo")
    print("0 - Sair")


while True:
    menu()
    op = input("Opcao: ").strip()

    if op == "1":
        v = input("Nome do vertice: ").strip().upper()
        inserir_vertice(v)

    elif op == "2":
        v = input("Vertice que vai remover: ").strip().upper()
        remover_vertice(v)

    elif op == "9":
        mostrar_grafo()

    elif op == "0":
        print("Saindo...")
        break

    else:
        print("Opcao invalida")
