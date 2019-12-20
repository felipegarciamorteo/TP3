#!/usr/bin/python3
import string
import sys
from grafo import Grafo
import biblioteca_grafo
import heapq
import csv
from collections import deque
import operator

no_dirigido = 1
dirigido = 0
ciudades = {}#creo un diccionario para saber los aeropuertos de cada ciudad
flecha = " -> "
coma = ", "

def imprimir_resultado(res,sep):
    resultado = res.pop(len(res)-1)
    while len(res) > 0:
        resultado += flecha + res.pop(len(res)-1)
    print(resultado)

def imprimir_parar_atras(camino,destino):
    anterior = camino[destino]
    resultado = anterior + flecha + destino
    while camino[anterior] is not None:
        anterior = camino[anterior]
        resultado = anterior + flecha + resultado
    print(resultado)

def camino_mas(parametros,flycombi):
    if len(parametros) != 3 or parametros[1] not in ciudades or parametros[2] not in ciudades: return False 
    if parametros[0] == "rapido":
        peso = "tiempo"
    elif parametros[0] == "barato":
        peso = "precio"
    else: return False
    min = float('inf')
    
    for aerop in ciudades[parametros[1]]:
            dest,camino,costo = biblioteca_grafo.dijkstra_flycombi(flycombi,aerop,parametros[2],peso,ciudades)
            if costo < min:
                min = costo
                camino_final = camino
                dest_final = dest
    if not dest: return False

    imprimir_parar_atras(camino_final,dest_final)
    return True

def camino_escalas(parametros,flycombi):
    if len(parametros) != 2 or parametros[0] not in ciudades or parametros[1] not in ciudades: return False 
    min = float('inf')
    for aerop in ciudades[parametros[0]]:
            padre, orden = biblioteca_grafo.bfs(flycombi,aerop)
            for aerop1 in ciudades[parametros[1]]:
                if orden[aerop1] < min:
                    min = orden[aerop1]
                    camino_final = padre
                    aerop_final = aerop1
    if min == float('inf'): return False

    imprimir_parar_atras(camino_final,aerop_final)
    return True

def centralidad(parametros,flycombi):
    if len(parametros) != 1 or not parametros[0].isnumeric() or int(parametros[0]) <= 0 or int(parametros[0]) > len(flycombi.vertices) : return False
    
    cent = {}
    for v in flycombi.vertices: cent[v] = 0
    for v in flycombi.vertices:
        padre, distancia = biblioteca_grafo.dijkstra_flycombi(flycombi,v,None,"frecuencia",ciudades)
        cent_aux = {}
        for w in flycombi.vertices: cent_aux[w] = 0
        
        vertices_ordenados = sorted(distancia.items(),key=operator.itemgetter(1),reverse = True)
        for w in vertices_ordenados:
            if w == float('inf') or padre[w[0]] is None: continue
            cent_aux[padre[w[0]]] += 1 + cent_aux[w[0]]
        for w in flycombi.vertices:
            if w == v: continue
            cent[w] += cent_aux[w]

    res = sorted(cent.items(),key=operator.itemgetter(1))
    resultado = (res.pop()[0])
    for i in range(1,int(parametros[0])):
        desencolado = res.pop()
        resultado += coma + desencolado[0]
    print(resultado)
    return True


def centralidad_aprox(parametros,flycombi):
    return 

def pagerank(parametros,flycombi):
    return

def nueva_aerolinea(parametros,flycombi):
    if len(parametros) != 1 : return False 
    rutas = biblioteca_grafo.prim_flycombi(flycombi,"precio")
    visitados = set()
    with open (parametros[0],'w') as aerolinea:
        f_writer = csv.writer(aerolinea)
        for v in rutas[0].vertices:
            for a in rutas[0].adyacentes(v):
                if (a,v) in visitados: continue
                visitados.add((v,a))
                p = rutas[0].peso(v,a)
                f_writer.writerow([v,a,p.tiempo,p.precio,p.cantidad])
    print("OK")
    return True



def viaje_valido(viaje,flycombi,visitados):
    estuvo = False
    for i in ciudades:
        for j in ciudades[i]:
            if j in visitados: 
                estuvo = True
        if not estuvo: return False
        estuvo = False
    return True

'''def recorrer_mundo_bt(v,flycombi,visitados,res,costo):
    visitados.add(flycombi.dato(v,'ciudad'))
    heap = []
    for w in flycombi.adyacentes(v):
        heapq.heappush(heap,(flycombi.peso(v,w).tiempo,v,w))
    while len(heap) > 0:
        peso,orig,dest = heapq.heappop(heap)
        if flycombi.dato(dest,'ciudad') in visitados: continue
        visitados.add(flycombi.dato(w,'ciudad'))
        costo += intAR
(peso)
        #print(w)
        res += "->"+w
        #print(res)
        res,costo = recorrer_mundo_bt(w,flycombi,visitados,res,costo)
        for x in flycombi.adyacentes(w):
            if flycombi.dato(x,'ciudad') not in visitados:
                heapq.heappush(heap,(flycombi.peso(w,x).tiempo,w,x))
        #print(flycombi.dato(w,'ciudad'))
    return res,costo'''

def recorrer_mundo_bt(v,flycombi,visitados,camino_act,costo,estaba):
    #print (len(ciudades),len(visitados))
    
    visitados.add(v)
    if len(ciudades) == len(visitados):
        #print("entro")
        if viaje_valido(camino_act,flycombi,visitados):
            #print("es valido")rec
            return res,costo 
        else:
            if not estaba:   
                visitados.remove(v)
            return None
    for w in flycombi.adyacentes(v):
        #if flycombi.dato(w,'ciudad') in visitados: continue
        #costo += int(flycombi.peso(v,w).tiempo)
        #print(w)
        #print(res)
        if w in visitados:
            res,costo = recorrer_mundo_bt(w,flycombi,visitados,camino_act+[w],costo+int(flycombi.peso(v,w).tiempo),True)
        else:
            res,costo = recorrer_mundo_bt(w,flycombi,visitados,camino_act+[w],costo+int(flycombi.peso(v,w).tiempo),False)
        if res is not None:
            return res,costo
        #print(flycombi.dato(w,'ciudad'))
    if not estaba:
        visitados.remove(w)
    return None

def es_conexo(grafo):
    padre,orden = biblioteca_grafo.bfs(grafo,grafo.vertice_random())
    return len(padre) == len(grafo.vertices)

def recorrer_mundo(parametros,flycombi):#back_tracking
    if len(parametros) != 1 or parametros[0] not in ciudades or not es_conexo(flycombi): return False
    min = float('inf')
    '''for v in ciudades[parametros[0]]:
        res,costo = biblioteca_grafo.prim_flycombi(flycombi,v)
        if min > costo:
            min = costo
            sol = res
            orig = v      
    print (sol)
        
    print(costo)'''
    #while len(visitados) != len(ciudades):
    resultado = None
    for origen in ciudades[parametros[0]]:
        recorrido,tardo = biblioteca_grafo.prim_flycombi(flycombi,origen)
        if min > tardo:
            min = tardo
            resultado = recorrido
    if resultado is None: return False #recorrido'''
    '''resultado = res.pop(len(res)-1)
    while len(res) > 0:
        resultado += "->" + res.pop(len(res)-1)'''
    
    #imprimir_resultado(res)
    for i in resultado.vertices:
        print("ciudad:",i)
        for j in resultado.adyacentes(i):
            print("ady:",j)
    print(tardo)
    return True

def recorrer_mundo_aprox(parametros,flycombi):
    return

def vacaciones(parametros,flycombi):
    if len(parametros) != 2 or parametros[0] not in ciudades or not parametros[1].isnumeric() : return False

    for origen in ciudades[parametros[0]]:
        resultado = biblioteca_grafo.ciclo_n(flycombi,origen,origen,int(parametros[1]),set(),[origen])
        if resultado is not None:
            print(flecha.join(resultado+[origen]))
            return True
    print("No se encontro recorrido")
    return True

def itinerario(parametros,flycombi):
    if len(parametros) != 1 : return False 
    with open (parametros[0],'r') as itinerario_actual:
        reader = csv.reader(itinerario_actual,delimiter=',')
        prim = True
        a_visitar = []
        restriccion = []
        for linea in reader:
            if prim == True:
                prim = False
                for ciudad in linea:
                    a_visitar.append(ciudad)
            else:
                restriccion.append([linea[0],linea[1],1])
    grafo_itinerario = Grafo(dirigido,a_visitar,restriccion)
    ordenados = biblioteca_grafo.orden_topologico(grafo_itinerario)
    print(coma.join(ordenados))
    for i in range(len(ordenados)-1):
        parametros = [ordenados[i],ordenados[i+1]]
        camino_escalas(parametros,flycombi)
    return True

def exportar_kml(parametros,flycombi):
    return



def identificar_operacion(comando,flycombi):
    if len(comando) > 1:
        parametros = comando[1].split(",")
    elif comando[0] != "listar_operaciones": return False

    if comando[0] == "listar_operaciones":
        print("camino_mas")
        print("camino_escalas")
        print("centralidad")
        print("nueva_aerolinea")
        #print("recorrer_mundo")
        print("vacaciones")
        print("itinerario")
    elif comando[0] == "camino_mas":
        if not camino_mas(parametros,flycombi): return False
    elif comando[0] == "camino_escalas":
        if not camino_escalas(parametros,flycombi): return False
    elif comando[0] == "centralidad":
        if not centralidad(parametros,flycombi): return False
    elif comando[0] == "centralidad_aprox":
        if not centralidad_aprox(parametros,flycombi): return False
    elif comando[0] == "pagerank" :
        if not pagerank(parametros,flycombi): return False
    elif comando[0] == "nueva_aerolinea" :
        if not nueva_aerolinea(parametros,flycombi): return False
    elif comando[0] == "recorrer_mundo" :
        if not recorrer_mundo(parametros,flycombi): return False
    elif comando[0] == "recorrer_mundo_aprox" :
        if not recorrer_mundo_aprox(parametros,flycombi): return False
    elif comando[0] == "vacaciones" :
        if not vacaciones(parametros,flycombi): return False
    elif comando[0] == "itinerario" :
        if not itinerario(parametros,flycombi): return False
    elif comando[0] == "exportar_kml":
        if not exportar_kml(parametros,flycombi): return False
    else: 
        return False
    return True


'''MAIN/APENAS ABRE EL PROGRAMA'''

def main():
    if len(sys.argv) != 3:
        print("Cantidad de parámetros errónea")
        return

    flycombi = Grafo(no_dirigido)

    with open(sys.argv[1],'r') as aeropuertos:
        reader = csv.reader(aeropuertos,delimiter=',')
        for linea in reader:
            if linea[0] in ciudades:
                ciudades[linea[0]].append(linea[1])
            else:
                ciudades[linea[0]] = [linea[1]]
            #vertices.append(linea[1])#guardo solo los aeropuertos
            flycombi.agregar_vertice(linea[1])
            flycombi.agregar_dato(linea[1],'ciudad',linea[0]) 

    with open(sys.argv[2],'r') as vuelos:
        reader = csv.reader(vuelos,delimiter=',')
        for linea in reader:
            peso = biblioteca_grafo.Peso(linea[2],linea[3],linea[4])
            #aristas.append((linea[0],linea[1],peso))
            flycombi.agregar_arista(linea[0],linea[1],peso)

    for operacion in sys.stdin:
        if operacion[-1] == '\n':
            operacion = operacion[:-1]
        comando = operacion.split(" ",1)
        if not identificar_operacion(comando,flycombi):
            print("Error en comando",comando[0])
    return


main()
