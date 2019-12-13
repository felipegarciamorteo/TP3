from grafo import Grafo
import biblioteca_grafo

ej = Grafo()

ej.agregar_vertice('a')
ej.agregar_vertice('c')

print ("vertice a pertenece",ej.pertenece('a'))
print ("vertice b pertenece",ej.pertenece('b'))

ej.agregar_vertice('f')
ej.agregar_vertice('h')
ej.agregar_vertice('r')
ej.agregar_arista('a','c',2)
ej.agregar_arista('f','r',7)
ej.agregar_arista('f','h',3)
ej.agregar_arista('a','f',4)
ej.agregar_arista('c','r',5)

padres,dist = biblioteca_grafo.dijkstra(ej,'a')
print("DIJKSTRA\n")
print(padres)
print(dist)

p,d = biblioteca_grafo.dijkstra_final(ej,'a','r')
print("DIJKSTRA CON DESTINO")
print(p)
print(d)


for v in ej.vertices:
    print (v,", sus adyacentes:")
    for w in ej.adyacentes(v,0):
        print ('\t',w)



print ("vertice aleatorio:",ej.vertice_random())

print("vertice h pertenece",ej.pertenece('h'))
print ("elimino vertice h:",ej.eliminar_vertice('h'))
print ("vertice h ya no pertenece",not ej.pertenece('h'))

try:
    ej.agregar_vertice(no_estoy_definido)
    print("se pudo guardar vertice sin clave cadena")
except:
    print ("No se pudo guardar vertice sin clave cadena, ni tampoco definido")

print("La arista que va de f a r existe y su peso es:",ej.peso('f','r'))
print("los adyacentes de f son:",ej.adyacentes('f',0))

print("elimine la arista:",ej.eliminar_arista('f','r'))
print("los adyacentes de f ahora son:",ej.adyacentes('f',not None))


'''creo un grafo dirigido'''
print("\n\ncreo un grafo dirigido\n")
dirig = Grafo(0)

dirig.agregar_vertice('a')
dirig.agregar_vertice('c')

dirig.agregar_arista('a','c',16)
dirig.agregar_arista('a','f',7)
dirig.agregar_arista('c','a',3)

for v in dirig.vertices:
    print (v,", sus adyacentes:")
    for w in dirig.adyacentes(v,0):
        print ('\t',w)


''' creo una lista con vertices para crear un grafo con los mismos'''
print("\n\ncreo una lista con vertices y una con aristas para crear un grafo con los mismos\n")
vertices = ['g','e','m','j','w']
aristas = [('g','e'),('w','j',3),('m','g',1)]


g = Grafo(1,vertices,aristas)

for v in g.vertices:
    print ("\nvertice:",v,"\nAdyacentes de",v,":")
    for w in g.adyacentes(v,1):
        print(w)