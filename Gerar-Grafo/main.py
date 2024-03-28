#Gerar Grafo

import networkx as nx
import matplotlib.pyplot as plt

def criar_grafo_exemplo():
    G = nx.Graph()

   # Adiciona nós
    G.add_nodes_from(["A", "B", "C", "D", "E", "F"])

    # Adiciona arestas
    G.add_edges_from([("A", "B"), ("A", "C"), ("B", "C"), ("C", "D"), ("C", "F"), ("D", "E"), ("E", "F"), ("F", "A"), ("F", "D")])

    return G

def desenhar_grafo(grafo):
    pos = nx.spring_layout(grafo)  # Define a posição dos nós
    nx.draw(grafo, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=10)
    plt.show()

grafo_exemplo = criar_grafo_exemplo()

desenhar_grafo(grafo_exemplo)

#Algoritmo de Busca - "Busca Cega"

from collections import deque

def busca_largura(grafo, inicio, objetivo):
    fila = deque([(inicio, [inicio])])
    print(str(fila))

    while fila:
        (vertice, caminho) = fila.popleft()
        print("vertice: " + str(vertice))
        print("caminho: " + str(caminho))
        for vizinho in grafo[vertice]:
            print("vizinho: " + str(vizinho))
            if vizinho not in caminho:
                if vizinho == objetivo:
                    return caminho + [vizinho]
                else:
                    fila.append((vizinho, caminho + [vizinho]))

fila = deque([('A', ['A'])])
print(str(fila))
(vertice, caminho) = fila.popleft()
print(str((vertice, caminho)))

grafo_exemplo = {
    "A": ["B", "C"],
    "B": ["A", "C", "E"],
    "C": ["A", "F", "D"],
    "D": ["B", "E"],
    "E": ["B", "H"],
    "F": ["C", "A"],
}

resultado = busca_largura(grafo_exemplo, 'A', 'H')
print("Caminho mais curto:", resultado)