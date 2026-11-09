vertices = []
arestas = []
direcionado = False


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
    print("Vertice", v, "inserido")


def remover_vertice(v):
    if v not in vertices:
        print("Vertice nao encontrado")
        return
    vertices.remove(v)

    i = 0
    while i < len(arestas):
        if arestas[i][0] == v or arestas[i][1] == v:
            arestas.pop(i)
        else:
            i += 1
    print("Vertice", v, "removido")


def posicao_aresta(x, y):
    for i in range(len(arestas)):
        a, b = arestas[i]
        if a == x and b == y:
            return i
        if not direcionado and a == y and b == x:
            return i
    return -1


def existe_aresta(x, y):
    return posicao_aresta(x, y) != -1


def inserir_aresta(x, y):
    if x not in vertices or y not in vertices:
        print("Um dos vertices nao existe, insere ele primeiro")
        return
    if existe_aresta(x, y):
        print("Essa aresta ja existe")
        return

    arestas.append((x, y))
    print("Aresta", x, "-", y, "inserida")


def remover_aresta(x, y):
    i = posicao_aresta(x, y)
    if i == -1:
        print("Essa aresta nao existe")
        return
    arestas.pop(i)
    print("Aresta removida")


def mostrar_graus():
    if len(vertices) == 0:
        print("Grafo vazio")
        return

    for v in vertices:
        if direcionado:
            saida = 0
            entrada = 0
            for a, b in arestas:
                if a == v:
                    saida += 1
                if b == v:
                    entrada += 1
            print(v, "-> entrada:", entrada, "| saida:", saida, "| total:", entrada + saida)
        else:
            grau = 0
            for a, b in arestas:
                if a == v:
                    grau += 1
                if b == v:
                    grau += 1
            print(v, "-> grau", grau)


def vizinhos(v):
    lista = []
    for a, b in arestas:
        if a == v:
            lista.append(b)
        elif not direcionado and b == v:
            lista.append(a)
    return lista


def verificar_percurso(caminho):
    if len(caminho) < 2:
        print("Digita pelo menos 2 vertices")
        return

    for v in caminho:
        if v not in vertices:
            print("O vertice", v, "nao existe no grafo")
            return

    for i in range(len(caminho) - 1):
        if not existe_aresta(caminho[i], caminho[i + 1]):
            print("Percurso NAO e possivel, nao tem aresta de", caminho[i], "para", caminho[i + 1])
            return

    print("Percurso possivel!")


def mostrar_arestas():
    if len(vertices) == 0:
        print("Grafo vazio")
        return

    print("Vertices:", ", ".join(vertices))
    if len(arestas) == 0:
        print("Nenhuma aresta")
        return

    seta = "->" if direcionado else "--"
    print("Arestas:")
    for i in range(len(arestas)):
        a, b = arestas[i]
        print(" ", i + 1, ":", a, seta, b)


def menu():
    print()
    print("------ GRAFO (Lista de Arestas) ------")
    print("1 - Inserir vertice")
    print("2 - Remover vertice")
    print("3 - Inserir aresta")
    print("4 - Remover aresta")
    print("5 - Mostrar grau dos vertices")
    print("6 - Verificar se existe aresta")
    print("7 - Listar vizinhos de um vertice")
    print("8 - Verificar percurso")
    print("9 - Mostrar lista de arestas")
    print("0 - Sair")


resp = input("O grafo e direcionado? (s/n): ").strip().lower()
while resp not in ("s", "sim", "n", "nao", "não"):
    print("Responde so com s ou n")
    resp = input("O grafo e direcionado? (s/n): ").strip().lower()
direcionado = resp in ("s", "sim")

while True:
    menu()
    op = input("Opcao: ").strip()

    if op == "1":
        v = input("Nome do vertice: ").strip().upper()
        inserir_vertice(v)

    elif op == "2":
        v = input("Vertice que vai remover: ").strip().upper()
        remover_vertice(v)

    elif op == "3":
        x = input("Vertice de origem: ").strip().upper()
        y = input("Vertice de destino: ").strip().upper()
        inserir_aresta(x, y)

    elif op == "4":
        x = input("Vertice de origem: ").strip().upper()
        y = input("Vertice de destino: ").strip().upper()
        remover_aresta(x, y)

    elif op == "5":
        mostrar_graus()

    elif op == "6":
        x = input("De qual vertice: ").strip().upper()
        y = input("Para qual vertice: ").strip().upper()
        if x not in vertices or y not in vertices:
            print("Um dos vertices nao existe no grafo")
        elif existe_aresta(x, y):
            print("Existe aresta de", x, "para", y)
        else:
            print("Nao existe aresta de", x, "para", y)

    elif op == "7":
        v = input("Vertice: ").strip().upper()
        if v not in vertices:
            print("Vertice nao encontrado")
        else:
            viz = vizinhos(v)
            if len(viz) == 0:
                print(v, "nao tem vizinhos")
            else:
                print("Vizinhos de", v + ":", ", ".join(viz))

    elif op == "8":
        caminho = input("Digita o percurso separado por espaco (ex: A B C): ").upper().split()
        verificar_percurso(caminho)

    elif op == "9":
        mostrar_arestas()

    elif op == "0":
        print("Saindo...")
        break

    else:
        print("Opcao invalida")
