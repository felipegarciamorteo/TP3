#encoding: utf-8(para las ñ)
import grafo
import heapq


#camino_mas rapido/barato
def dijkstra(grafo,origen): 
    padres = {}
    dist = {}
    for i in grafo.vertices():
        dist[i] = float('inf')
        padres[i] = None
    padres[origen] = None
    dist[origen] = 0
    heap = heap.crear()
    heap.encolar((None,origen,0))
    while not heap.vacio:
        v,w,l = heap.desencolar()
        for in grafo.adyacentes(w)
            if (dist[v]+l) < dist[w]:
                dist[w] = dist[v]+l
                padres[w] = v
                heap.encolar() 



#camino_escalas
def bfs(grafo):

def dfs(grafo):
    

#  
def centralidad(grafo):



def prim(grafo):



def kruskal(grafo):
