from grafo_code.grafo import Grafo
from grafo_code.graficar_grafo import graficar_pyvis, graficar_nx
from euristica import calcular_h

g = Grafo(dirigido=False, ponderado=True)
g.agregar_arista("a", "b", 3)
g.agregar_arista("a", "c", 4)

g.agregar_arista("b", "d", 6)
g.agregar_arista("b", "e", 5)

g.agregar_arista("c", "e", 6)

g.agregar_arista("e", "d", 2)
g.agregar_arista("e", "z", 12)

g.agregar_arista("d", "z", 7)

posiciones = {
    'a': [0,1],
    'b': [2,2],
    'c': [2,0],
    'd': [4,2],
    'e': [4,0],
    'z': [6,1]
}

h = calcular_h(posiciones, 'z')

#graficar_nx(g)
#graficar_pyvis(g)

ruta_bfs = g.bfs("c", "z")
print("Ruta BFS\n", ruta_bfs)

ruta_dfs = g.dfs("c", "z")
print("\nRuta DFS\n", ruta_dfs)

ruta_dijkstra = g.dijkstra("c", "z")
print("\nRuta Dijkstra\n", ruta_dijkstra)

ruta_a_estrella = g.a_estrella("c", "z", h)
print("\nRuta A*\n", ruta_a_estrella)