# 0 == não visitado
# 1 == em percurso
# 2 == visitado
# To-do: Usar ENUM e também fazer implementação usando classes. 
def receber_grafo():
    numero_vertices = int(input("Quantos vértices terão seu grafo?"))
    Grafo = [([0]*numero_vertices) for i in range(numero_vertices)]
    for vertice in range(numero_vertices):
        while True:
            aresta = int(input(f"O vértice {vertice} é vizinho de qual vértice? Digite -1 para finalizar"))
            if aresta == -1:
                    break
            else: 
                    Grafo[vertice][aresta] = 1
                    Grafo[aresta][vertice] = 1
    return Grafo
            
def DFS(Grafo, vertice_inicial, numero_vertices):
    estados = [0]*numero_vertices
    visitados = []
    visitados.append("Componente 1:")
    DFS_rec(Grafo, vertice_inicial, estados, visitados)
    i = 1
    while len(visitados) != numero_vertices + i:
        i = i + 1
        visitados.append(f"Componente {i}:")
        for vertice, estado in enumerate(estados):
            if estado == 0: 
                DFS_rec(Grafo, vertice, estados, visitados)
    print(visitados)
def DFS_rec(Grafo, vertice: int, estados: list, visitados: list):
    estados[vertice] = 1
    visitados.append(vertice)
    for vizinho, aresta in enumerate(Grafo[vertice]):
        if (aresta == 1) and (estados[vizinho] == 0):
                DFS_rec(Grafo, vizinho, estados, visitados)
    estados[vertice] = 2
    
Grafo = receber_grafo()
DFS(Grafo, 0, 6)
