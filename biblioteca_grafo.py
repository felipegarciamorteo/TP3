#encoding: utf-8(para las ñ)
from grafo import Grafo
import heapq
from collections import deque

'''TENER CUIDADO CON LAS VARIABLES QUE SE REPITEN, NO PASA NADA?'''
class Peso():
    def __init__(self,tiempo,precio,cantidad):
        self.tiempo = tiempo
        self.precio = precio
        self.cantidad = cantidad
    
#camino_mas rapido/barato
def dijkstra(grafo,origen): 
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
        for w in grafo.adyacentes(v):
            if dist[v]+grafo.peso(v,w) < dist[w]:
                dist[w] = dist[v] + grafo.peso(v,w)
                padre[w] = v
                heapq.heappush(heap,(dist[w],w))
    return padre,dist

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

        if v in ciudades[destino]:
            return v,padre,dist[v]
        for w in grafo.adyacentes(v):
            #print("ciudad:",w)
            if tipo == "tiempo":
                p = int(grafo.peso(v,w).tiempo)
            elif tipo == "precio":
                p =  int(grafo.peso(v,w).precio)
            #print(distv,"de ")
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

def dfs_recursivo(grafo,v,vis,padre,orden):
    vis.add(v)
    for w in grafo.adyacentes(v):
        if w not in vis:
            padre[w] = v
            orden[w] = orden[v] + 1
            dfs_recursivo(grafo,w,vis,padre,orden)


def dfs(grafo):
    visitados = set()
    padre = {}
    orden = {}
    for v in grafo:
        if v not in visitados:
            orden[v] = 0
            padre[v] = None
            dfs_recursivo(grafo,v,visitados,padre,orden)
    return padre,orden

def centralidad(grafo):
    cent = {}
    for v in grafo: cent[v] = 0
    for v in grafo:
        # hacia todos los demas vertices
        distancia, padre = dijkstra(grafo, v)
        cent_aux = {}
        for w in grafo: cent_aux[w] = 0
        # Aca filtramos (de ser necesario) los vertices a distancia infinita, 
        # y ordenamos de mayor a menor
        vertices_ordenados = ordenar_vertices(grafo, distancias) 
        for w in vertices_ordenados:
            cent_aux[padre[w]] += 1 + cent_aux[w]
        # le sumamos 1 a la centralidad de todos los vertices que se encuentren en 
        # el medio del camino
        for w in grafo:
            if w == v: continue
            cent[w] += cent_aux[w]
    return cent


def centralidad_aprox(grafo):
    cent = {}
    for v in grafo:
        cent[v] = 0
    for v in grafo:
        for w in grafo:
            if v == w: continue
            #padre,distancia = camino_minimo(grafo,v,w)
            padre = camino_minimo(grafo,v,w)
            if padre[w] is None: continue
            actual = padre[w]
            while actual != v:
                cent[actual] += 1
                actual = padre[actual]
    return cent



def prim(grafo):
    vertice = grafo.vertice_random()
    visitados = set()
    visitados.add(vertice)
    heap = []
    for w in grafo.adyacentes(vertice):
        heapq.heappush(heap,(vertice,w,grafo.peso(vertice,w)))
    arbol = grafo()
    while len(heap) > 0:
        v,w,p = heapq.heappop(heap)
        if w in visitados: continue
        arbol.agregar_arista(v,w,p)
        visitados.add(w)
        for x in grafo.adyacentes(w):
            if x not in visitados:
                heapq.heappush(heap,(w,x,grafo.peso(w,x)))
    return arbol

def prim_flycombi(grafo,vertice = None):
    if vertice == None:
        vertice = grafo.vertice_random()
    costo = 0
    visitados = set()
    visitados.add(vertice)
    heap = []
    for w in grafo.adyacentes(vertice):
        heapq.heappush(heap,(vertice,w,grafo.peso(vertice,w).tiempo))
    arbol = vertice
    while len(heap) > 0:
        v,w,p = heapq.heappop(heap)
        if w in visitados: continue
        arbol += "->"+w
        costo += int(p)
        visitados.add(w)
        for x in grafo.adyacentes(w):
            if x not in visitados:
                heapq.heappush(heap,(w,x,grafo.peso(w,x).tiempo))
    return arbol,costo
#recorrido n

def recorrido_n(grafo, n, origen):
    visitados = set()
    padre = {}
    orden = {}
    cont = 0
    return n_recursivo(grafo,origen ,visitados ,padre ,orden, cont, n, origen)
    

def n_recursivo(grafo, v, vis, padre, orden, cont, n, origen):
    vis.add(v)
    for w in grafo.adyacentes(v):
        if (w not in vis and cont<n) or (cont == n  and  w  == origen):
            padre[w] = v
            orden[w] = orden[v] + 1
            cont = cont + 1
            if  w != origen:
                n_recursivo(grafo,w,vis,padre,orden,cont, n, origen)
            else: 
                return padre, orden 
    del padre[v]
    del orden[v]
    vis.remove[v]
    
def kruskal(grafo):
    return 
