#encoding: utf-8(para las ñ)
import grafo
import heapq
from collections import deque

'''TENER CUIDADO CON LAS VARIABLES QUE SE REPITEN, NO PASA NADA?'''


#camino_mas rapido/barato
def dijkstra(grafo,origen): 
    padre = {}
    dist = {}
    for i in grafo:
        dist[i] = float('inf')
    padre[origen] = None
    dist[origen] = 0
    heap = [(0,origen)]
    while len(heap) > 0:
        v = heapq.heappop(heap)
        for w in grafo.adyacentes(v):
            if (dist[v]+grafo.peso(v,w)) < dist[w]:
                dist[w] = dist[v] + grafo.peso(v,w)
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

def kruskal(grafo):
    return 