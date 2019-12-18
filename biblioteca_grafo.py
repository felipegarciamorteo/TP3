#encoding: utf-8(para las ñ)
from grafo import Grafo
import heapq
from collections import deque

'''TENER CUIDADO CON LAS VARIABLES QUE SE REPITEN, NO PASA NADA?'''

#-----CLASE PARA DIFERENCIAR EL PESO DE LAS ARISTAS DEL GRAFO SEGÚN LA OPERACIÓN------

class Peso():
    def __init__(self,tiempo,precio,cantidad):
        self.tiempo = tiempo
        self.precio = precio
        self.cantidad = cantidad
    

#-----------------CAMINOS MÍNIMOS---------------------

#camino_mas
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

        if destino is not None:
            if v in ciudades[destino]:
                return v,padre,dist[v]
        for w in grafo.adyacentes(v):
            #print("ciudad:",w)
            if tipo == "tiempo":
                p = int(grafo.peso(v,w).tiempo)
            elif tipo == "precio":
                p =  int(grafo.peso(v,w).precio)
            elif tipo == "frecuencia":
                p = 1/int(grafo.peso(v,w).cantidad) 
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

        
#-------------------CENTRALIDAD-------------------

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

#--------------ARBOLES DE TENDIDO MINIMO--------------------

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

def kruskal(grafo):
    return 

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
    

#--------------ALGORITMO TOP K-----------------------

def top_k(datos,n,k):
    heap = []
    res = []
    cont = 0
    for clave,valor in datos.items():
        if cont < k:
            heapq.heappush(heap,(clave,valor))
            cont += 1
        else: 
            #tope = heapq.nsmallest(1,heap)
            if valor > ((heap[0])[1]):
                heapq.heappop(heap)
                heapq.heappush(heap,(clave,valor))
                cont += 1
    while len(heap) > 0:
        res.append((heapq.heappop(heap)[0]))
    print(res)
    return res



#----------- ORDENAMIENTOS COMPARATIVOS----------------

# -*- coding: utf-8 -*-

from time import time

def mergeSort(lista):
    if len(lista) <= 1:
        return lista

    medio = int(len(lista)) / 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    izquierda = mergeSort(izquierda)
    derecha = mergeSort(derecha)

    return merge(izquierda, derecha)

def merge(listaA, listaB):
    global comparaciones
    lista_nueva = []
    a = 0
    b = 0

    while a < len(listaA) and b < len(listaB):
        comparaciones += 1

        if listaA[a] < listaB[b]:
            lista_nueva.append(listaA[a])
            a += 1
        else:
            lista_nueva.append(listaB[b])
            b += 1

    while a < len(listaA):
        lista_nueva.append(listaA[a])
        a += 1

    while b < len(listaB):
        lista_nueva.append(listaB[b])
        b += 1

    return lista_nueva

def bubbleSort(lista):
    n = len(lista)
    for i in range(1, n):
        for j in range(n-i):
            if lista[j] < lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def insertionSort(lista):
    n = len(lista)

    for i in range(1, n):
        val = lista[i]
        j = i

        while j > 0 and lista[j-1] > val:
            lista[j] = lista[j-1]
            j -= 1

        lista[j] = val
    return lista
