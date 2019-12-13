#encoding: utf-8(para las ñ)
import sys
from grafo import Grafo
import biblioteca_grafo
import heapq
import csv
from collections import deque
import fileinput

no_dirigido = 1
ciudades = {}#creo un diccionario para saber los aeropuertos de cada ciudad
'''TENER CUIDADO CON LAS VARIABLES QUE SE REPITEN, NO PASA NADA?'''

def camino_mas(parametros,flycombi):
    if len(parametros) != 3 or parametros[1] not in ciudades or parametros[2] not in ciudades: return False 
    #print(parametros[0])
    if parametros[0] == "rapido":
        peso = "tiempo"
    elif parametros[0] == "barato":
        peso = "precio"
    else: return False
    #camino = biblioteca_grafo.dijkstra_flycombi(flycombi,parametros[1],parametros[2],"precio",ciudades)
    min = float('inf')
    
    for aerop in ciudades[parametros[1]]:
            #print("oka,avanzamos")
            dest,camino,costo = biblioteca_grafo.dijkstra_flycombi(flycombi,aerop,parametros[2],peso,ciudades)
            if costo < min:
                min = costo
                camino_final = camino
                dest_final = dest
            #res = deque([parametros[2]])
    if not dest: return False

    
    anterior = camino_final[dest_final]
    resultado = anterior+"->"+dest_final
    while anterior not in ciudades[parametros[1]]:
        anterior = camino_final[anterior]
        resultado = anterior+"->"+resultado
        
        
        
    '''res = [dest_final]
    anterior = camino_final[dest_final]
    res.append(anterior)
    while anterior not in ciudades[parametros[1]]:
        anterior = camino_final[anterior]
        res.append(anterior)
    
    clave = res.pop(len(res)-1)

    while len(res) > 0:
        clave += "->" + res.pop(len(res)-1)
    print (clave)'''
    print(resultado)
    return True

def camino_escalas(parametros,flycombi):
    return

def centralidad(parametros,flycombi):
    return

def centralidad_aprox(parametros,flycombi):
    return 

def pagerank(parametros,flycombi):
    return

def nueva_aerolinea(parametros,flycombi):
    return 

def viaje_valido(viaje,flycombi,visitados):
    #for i in ciudades:
     #   if i not in visitados: return False
    '''for j in range(0,len(viaje)):
        if viaje[j+1] not in flycombi.adyacentes[j]: return False'''
    return True

'''def recorrer_mundo_bt(v,flycombi,visitados,res,costo):
    #print (len(ciudades),len(visitados))
    if len(ciudades) == len(visitados):
        #print("entro")
        if viaje_valido(res,flycombi,visitados):
            #print("es valido")
            return res,costo 
        return False
    for w in flycombi.adyacentes(v):
        if flycombi.dato(w,'ciudad') in visitados: continue
        visitados.add(flycombi.dato(w,'ciudad'))
        costo += int(flycombi.peso(v,w).tiempo)
        #print(w)
        res += "->"+w
        #print(res)
        res,costo = recorrer_mundo_bt(w,flycombi,visitados,res,costo)
        #print(flycombi.dato(w,'ciudad'))
    return res,costo'''

def recorrer_mundo_bt(v,flycombi,visitados,res,costo):
    visitados.add(flycombi.dato(v,'ciudad'))
    heap = []
    for w in flycombi.adyacentes(v):
        heapq.heappush(heap,(flycombi.peso(v,w).tiempo,v,w))
    while len(heap) > 0:
        peso,orig,dest = heapq.heappop(heap)
        if flycombi.dato(dest,'ciudad') in visitados: continue
        visitados.add(flycombi.dato(w,'ciudad'))
        costo += int(peso)
        #print(w)
        res += "->"+w
        #print(res)
        res,costo = recorrer_mundo_bt(w,flycombi,visitados,res,costo)
        for x in flycombi.adyacentes(w):
            if flycombi.dato(x,'ciudad') not in visitados:
                heapq.heappush(heap,(flycombi.peso(w,x).tiempo,w,x))
        #print(flycombi.dato(w,'ciudad'))
    return res,costo


def recorrer_mundo(parametros,flycombi):#back_tracking
    if len(parametros) != 1 or parametros[0] not in ciudades: return False

    min = float('inf')
    for v in ciudades[parametros[0]]:
        res,costo = biblioteca_grafo.prim_flycombi(flycombi,v)
        if min > costo:
            min = costo
            sol = res
            orig = v      
    print (sol)
        
    print(costo)
    '''visitados = set()
    #while len(visitados) != len(ciudades):
    
    for v in ciudades[parametros[0]]:
        res = v
        recorrido,tardo = recorrer_mundo_bt(v,flycombi,visitados,res,0)
        if min > tardo:
            min = tardo
            resultado = recorrido
    if not resultado: return False#recorrido'''
    '''resultado = res.pop(len(res)-1)
    while len(res) > 0:
        resultado += "->" + res.pop(len(res)-1)

    print(resultado)'''
    '''print(resultado)
    print(tardo)'''
    return True

def recorrer_mundo_aprox(parametros,flycombi):
    return

def vacaciones(parametros,flycombi):
    return 

def itinerario(parametros,flycombi):
    return 

def exportar_kml(parametros,flycombi):
    return



def identificar_operacion(comando,flycombi):
    print("hola")
    if len(comando) > 1:
        parametros = comando[1].split(",")
    elif comando[0] != "listar_operaciones": return False

    print(comando[0])
    if comando[0] == "listar_operaciones":
        listar_operaciones()
    elif comando[0] == "camino_mas":
        print("entro a identificar")
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
        print("esta en el else")
        return False
    return True
'''MAIN/APENAS ABRE EL PROGRAMA'''

def main():
    if len(sys.argv) != 3:
        print("Cantidad de parámetros errónea")
        return

    flycombi = Grafo(no_dirigido)
    '''vertices = []
    aristas = []'''

    with open(sys.argv[1],'r') as aeropuertos:
        reader = csv.reader(aeropuertos,delimiter=',')
        for linea in reader:
            #clave = linea[1]+","+linea[0]
            if linea[0] in ciudades:#ciudades.__contains__(linea[0]):
                ciudades[linea[0]].append(linea[1])
            else:
                ciudades[linea[0]] = [linea[1]]
            #vertices.append(linea[1])#guardo solo los aeropuertos
            #vertices.append(linea[1])
            flycombi.agregar_vertice(linea[1])
            flycombi.agregar_dato(linea[1],'ciudad',linea[0]) 

    with open(sys.argv[2],'r') as vuelos:
        reader = csv.reader(vuelos,delimiter=',')
        for linea in reader:
            peso = biblioteca_grafo.Peso(linea[2],linea[3],linea[4])
            #aristas.append((linea[0],linea[1],peso))
            flycombi.agregar_arista(linea[0],linea[1],peso)
        '''for linea in vuelos: 
            vue = linea.split(',')
            peso = biblioteca_grafo.Peso(vue[2],vue[3],vue[4])
            aristas.append((vue[0],vue[1],peso))'''

    #flycombi = Grafo(no_dirigido,vertices,aristas)

    '''for i in ciudades:
        for j in ciudades[i]:
            flycombi.agregar_dato(j,'ciudad',i)'''

    '''for comando in fileinput.input():
        comandos = linea'''

    operacion = input()
    #comando = readline
    while operacion and operacion != "exit" :#mientras siga habiendo lineas para procesar
        comando = operacion.split(" ",1)
        if not identificar_operacion(comando,flycombi):
            print("Error en comando",comando[0])
        operacion = input()
    


    ''' datos = input()
    archivos = datos.split(" ")
    print(datos)'''

    '''for s in archivos:
        print (s,len(s))


    for linea in fileinput.input():
        comandos = linea'''
    return


main()