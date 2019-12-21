from grafo import Grafo
import heapq
from collections import deque

#-----CLASE PARA DIFERENCIAR EL PESO DE LAS ARISTAS DEL GRAFO SEGÚN LA OPERACIÓN------

class Peso():
    def __init__(self,tiempo,precio,cantidad):
        self.tiempo = tiempo
        self.precio = precio
        self.cantidad = cantidad
    

#-----------------CAMINOS MÍNIMOS---------------------

def dijkstra_flycombi(grafo,origen,destino,tipo,ciudades):
    padre = {}
    dist = {}
    for i in grafo.vertices:
        dist[i] = float('inf')
    padre[origen] = None
    dist[origen] = 0
    heap = [(0,origen)]
    while len(heap) > 0:
        desencolado = heapq.heappop(heap)
        v = desencolado[1]

        if destino is not None:
            if v in ciudades[destino]:
                return v,padre,dist[v]
        for w in grafo.adyacentes(v):
            if tipo == "tiempo":
                p = int(grafo.peso(v,w).tiempo)
            elif tipo == "precio":
                p =  int(grafo.peso(v,w).precio)
            elif tipo == "frecuencia":
                p = 1/int(grafo.peso(v,w).cantidad)
            if dist[v] + p < dist[w]:
                dist[w] = dist[v] + p
                padre[w] = v
                heapq.heappush(heap,(dist[w],w))
    return padre,dist


#camino_escalas
def bfs(grafo,origen):
    visitados = set()
    padre = {}
    orden = {}
    cola = deque([])
    visitados.add(origen)
    padre[origen] = None
    orden[origen] = 0
    cola.append(origen)
    while len(cola) > 0:
        v = cola.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                cola.append(w)
                padre[w] = v
                orden[w] = orden[v] + 1
    return padre,orden

#--------------------TOPOLOGICO------------------
def orden_topologico(grafo):
    grado = {}
    for v in grafo.vertices:
        grado[v] = 0
    for v in grafo.vertices:
        for w in grafo.adyacentes(v):
            grado[w] +=1
    cola = deque([])
    for v in grafo.vertices:
        if grado[v] == 0:
            cola.append(v)
    resul = []
    while not len(cola) == 0:
        v = cola.popleft()
        resul.append(v)
        for w in grafo.adyacentes(v):
            grado[w] -= 1
            if grado[w] == 0:
                cola.append(w)
    if len(resul) == len(grafo.vertices):
        return resul
    else:
        return None

#--------------ARBOLES DE TENDIDO MINIMO--------------------

def prim_flycombi(grafo,peso,vertice = None):
    if vertice == None:
        vertice = grafo.vertice_random()
    costo = 0
    visitados = set()
    visitados.add(vertice)
    heap = []
    for w in grafo.adyacentes(vertice):
        arista = grafo.peso(vertice,w)
        if peso == "tiempo":
            heapq.heappush(heap,(int(arista.tiempo),vertice,w,arista))
        elif peso == "precio":
            heapq.heappush(heap,(int(arista.precio),vertice,w,arista))
    arbol = Grafo()
    while len(heap) > 0:
        p,v,w,a = heapq.heappop(heap)
        if w in visitados: continue
        arbol.agregar_arista(v,w,a)
        costo += int(p)
        visitados.add(w)
        for x in grafo.adyacentes(w):
            if x not in visitados:
                arista = grafo.peso(w,x)
                if peso == "tiempo":
                    heapq.heappush(heap,(int(arista.tiempo),w,x,arista))
                elif peso == "precio":
                    heapq.heappush(heap,(int(arista.precio),w,x,arista))
    return arbol,costo

#----------ENCONTRAR UN CICLO CON N VERTICES--------------

def ciclo_n(grafo,v,origen,n,vis,camino_actual):
    vis.add(v)
    if len(camino_actual) == n:
        if origen in grafo.adyacentes(v):
            return camino_actual
        else:
            vis.remove(v)
            return None 
    for w in grafo.adyacentes(v):
        if w in vis: continue
        solucion = ciclo_n(grafo,w,origen,n,vis,camino_actual+[w])
        if solucion is not None:
            return solucion
    vis.remove(v)
    return None