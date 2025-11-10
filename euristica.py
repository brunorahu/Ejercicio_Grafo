import numpy as np

def calcular_h(posiciones, destino):
    dest = np.array(posiciones[destino])
    h = {}
    for n, pos in posiciones.items():
        origen = np.array(pos)
        dist = np.linalg.norm(origen - dest)
        h[n] = dist
        
    return h