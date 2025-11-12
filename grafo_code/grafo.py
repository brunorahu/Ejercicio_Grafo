import heapq

class Grafo:
    def __init__(self, dirigido, ponderado):
        self.__dirigido = dirigido
        self.__ponderado = ponderado
        self.__lista_adj = {}
    
    def es_dirigido(self):
        return self.__dirigido
    
    def es_ponderado(self):
        return self.__ponderado
    
    def agregar_vertice(self, v):
        if v not in self.__lista_adj:
            self.__lista_adj[v] = {}
    
    def agregar_arista(self, origen, dest, peso=1):
        self.agregar_vertice(origen)
        self.agregar_vertice(dest)
        self.__lista_adj[origen][dest]=peso
        
        if not self.__dirigido:
            self.__lista_adj[dest][origen]=peso
            
    def vertices(self):
        return list(self.__lista_adj.keys())
    
    def vecinos(self, u):
        if u in self.__lista_adj:
            return list(self.__lista_adj[u].keys())
        
    def existe_arista(self, u, v):
        try:
            self.__lista_adj[u][v]
            return True
        except KeyError:
            return False
        
    def obtener_peso(self, u , v):
        if self.existe_arista(u,v):
            return self.__lista_adj[u][v]
        
    def orden(self):
        return len(self.__lista_adj.keys())
        
    def tamano(self):
        tamano = 0
        
        for n in self.__lista_adj:
            tamano += len(n)
    
        if not self.es_dirigido():
            tamano /= 2
        
        return tamano
    
    def grado(self, u):
        if self.__dirigido:
            return self.ingrado(u)+\
                self.outgrado(u)
        
        else:
            return len(self.__lista_adj[u])
        
    def outgrado(self, u):
        return len(self.__lista_adj[u])
    
    def ingrado(self, u):
        contador = 0
        for lista_nodo in self.__lista_adj:
            if u in lista_nodo:
                contador += 1
        return contador
    
    def aristas(self):
        lista = []
        for u, lista_vecinos in self.__lista_adj.items():
            for v in lista_vecinos.keys():
                if (u,v) not in lista and (v,u) not in lista:
                    lista.append((u,v))
        return lista
    
    def bfs(self, origen, dest):
        q = [(origen,[origen])]
        visitados = set()
        visitados.add(origen)
        
        while q:
            n_actual, r_actual = q.pop(0)
            if n_actual == dest:
                return r_actual
            
            for v in self.vecinos(n_actual):
                if v not in visitados:
                    visitados.add(v)
                    q.append((v, r_actual + [v]))
        
        return None
    
    def dfs(self, origen, dest):
        pila = [(origen, [origen])]
        visitados = set()
        
        while pila:
            n_actual, r_actual = pila.pop()
            
            if n_actual == dest:
                return r_actual
            
            if n_actual not in visitados:
                # Lo marcamos como visitado
                visitados.add(n_actual)
                
                # Agregamos todos sus vecinos a la pila para explorarlos
                for v in self.vecinos(n_actual):
                    if v not in visitados:
                        pila.append((v, r_actual + [v]))
        
        return None
    
    def dijkstra(self, origen, destino):
        costo = {
            n: float('inf')
            for n in self.vertices()
        }
        
        costo[origen] = 0
        
        prev = {
            n: None
            for n in self.vertices()
        }
        visitados = set()
        q = [(costo[origen], origen)]
        
        # Exploración
        while q:
            costo_u, u = heapq.heappop(q)
            if u in visitados:
                continue
            visitados.add(u)
            
            if u == destino:
                break
            for v in self.vecinos(u):
                costo_alt = costo_u + self.obtener_peso(u, v)
                if costo_alt < costo[v]:
                    costo[v] = costo_alt
                    prev[v] = u
                    heapq.heappush(q, (costo[v], v))
        
        if prev[destino] is None:
            return None, None
        
        actual = destino
        ruta = []
        while actual != None:
            ruta.append(actual)
            actual = prev[actual]
        return ruta[::-1], costo[destino]
    
    def a_estrella(self, origen, destino, h):
        # Inicialización
        g = {
            n: float('inf')
            for n in self.vertices()
        }
        g[origen] = 0
        f = {
            n: float ('inf')
            for n in self.vertices()
        }
        prev = {
            n: None
            for n in self.vertices()
        }
        q = [(f[origen], origen)]
        visitados = set()
        
        # Exploración
        while q:
            f_u, u = heapq.heappop(q)
            if u in visitados:
                continue
            if u == destino:
                break
            for v in self.vecinos(u):
                g_alt = g[u] + self.obtener_peso(u,v)
                if g_alt < g[v]:
                    g[v] = g_alt
                    prev[v] = u
                    f[v] = g[v] + h[v]
                    heapq.heappush(q, (f[v], v))
                    
        # Resultados
        if prev[destino] is None:
            return None, None
        actual = destino
        ruta = []
        
        while actual != None:
            ruta.append(actual)
            actual = prev[actual]
        return ruta[::-1], g[destino]
    
    def mst_prim(self, origen=None):
        vertices = self.vertices()
        if origen is None:
            origen = vertices[0]
        T = Grafo(
            dirigido = self.es_dirigido(),
            ponderado = self.es_ponderado()
        )
        T.agregar_vertice(origen)
        V = {
            v for v in vertices
        }
        V.remove(origen)
        
        # Construcción MST
        n = len(vertices)
        total = 0
        for i in range(n-1):
            aristas = []
            for u in T.vertices():
                for v in self.vecinos(u):
                    if v in V:
                        peso = self.obtener_peso(u, v)
                        aristas.append((peso, (u, v)))
                        
            aristas = sorted(aristas)
            menor_peso, (u, v) = aristas[0]
            total += menor_peso
            V.remove(v)
            T.agregar_arista(u,v, menor_peso)
        
        return T, total