vertices = []
matriz = []


def indice(v):
    if v in vertices:
        return vertices.index(v)
    return -1


def inserir_vertice(v):
    if v == "":
        print("Nome invalido")
        return
    if " " in v:
        print("O nome do vertice nao pode ter espaco")
        return
    if v in vertices:
        print("O vertice", v, "ja existe")
        return

    vertices.append(v)
    for linha in matriz:
        linha.append(0)
    matriz.append([0] * len(vertices))
    print("Vertice", v, "inserido")


def remover_vertice(v):
    i = indice(v)
    if i == -1:
        print("Vertice nao encontrado")
        return

    vertices.pop(i)
    matriz.pop(i) 
    for linha in matriz:
        linha.pop(i)  
    print("Vertice", v, "removido")


def mostrar_matriz():
    if len(vertices) == 0:
        print("Grafo vazio")
        return

    # largura da coluna depende do maior nome
    larg = 1
    for v in vertices:
        if len(v) > larg:
            larg = len(v)
    larg += 2

    print(" " * larg, end="")
    for v in vertices:
        print(v.rjust(larg), end="")
    print()
    for i in range(len(vertices)):
        print(vertices[i].rjust(larg), end="")
        for valor in matriz[i]:
            print(str(valor).rjust(larg), end="")
        print()


def menu():
    print()
    print("------ GRAFO (Matriz de Adjacencia) ------")
    print("1 - Inserir vertice")
    print("2 - Remover vertice")
    print("9 - Mostrar matriz")
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
        mostrar_matriz()

    elif op == "0":
        print("Saindo...")
        break

    else:
        print("Opcao invalida")
