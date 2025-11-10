import networkx as nx
from pyvis.network import Network
import matplotlib.pyplot as plt
from grafo_code.grafo import Grafo
import heapq

def graficar_pyvis(G: Grafo, archivo_html: str = "grafo.html") -> str:
    """
    Genera un HTML interactivo del grafo usando PyVis y devuelve la ruta al archivo.
    """
    net = Network(height="480px", width="100%", notebook=False, directed=G.es_dirigido())
    # Agrega nodos
    for u in sorted(G.vertices()):
        net.add_node(u, label=u, size=15, color='red')
    # Agrega aristas (con etiqueta de peso si es ponderado)
    for u, v in G.aristas():
        if G.es_ponderado():
            w = G.obtener_peso(u, v)
            net.add_edge(u, v, title=str(w), label=str(w))
        else:
            net.add_edge(u, v)
    # Física y opciones por defecto legibles
    #net.barnes_hut()
    net.write_html(archivo_html)
    return archivo_html
    
def graficar_nx(G):
    if G.es_dirigido:
        G_nx = nx.DiGraph()
    else:
        G_nx = nx.Graph()
        
    for u in G.vertices():
        G_nx.add_node(u)
    for u, v, in G.aristas():
        print(u, v)
        if G.es_ponderado():
            G_nx.add_edge(u, v, w=G.obtener_peso(u, v))
        else:
            G_nx.add_edge(u, v)

    # Diccionario de posiciones: nodo : (x, y)
    pos = nx.spring_layout(G_nx, seed=7) 

    plt.figure(figsize=(5,5))
    nx.draw(G_nx, pos=pos, with_labels=True, node_size=900, node_color='lime')
    nx.draw_networkx_edge_labels(G_nx, pos=pos)  # op
    #plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.show()