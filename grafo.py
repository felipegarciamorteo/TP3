import random

no_dirigido = 1

class Grafo():
    def __init__(self,tipo = no_dirigido,vertices = None,aristas = None):
        self.vertices = {}
        self.tipo = tipo
        if vertices != None:
            for i in vertices:
                self.agregar_vertice(i)
        if aristas != None:
            for j in aristas:
                if len(j) == 2: #Si es no pesado
                    self.agregar_arista(j[0],j[1])
                else:
                    self.agregar_arista(j[0],j[1],j[2])
        '''Vertices y aristas son listas con todos las aristas y vertices 
        del grafo para crear un grafo con elementos ya insertados'''

    def agregar_dato(self,vertice,clave,dato):
        self.vertices[vertice]['datos'][clave] = dato

    def dato(self,vertice,clave):
        return self.vertices[vertice]['datos'][clave]

    def agregar_vertice(self,vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}
            self.vertices[vertice]['ady'] = {}
            self.vertices[vertice]['datos'] = {}

    def eliminar_vertice(self,vertice):
        if vertice not in self.vertices: return None
        if self.tipo == no_dirigido:
            for i in self.vertices[vertice]['ady'].keys():
                self.vertices['ady'][i].pop(vertice)
        return self.vertices.pop(vertice,None)

    def agregar_arista(self,origen,destino,peso = None):
        if origen not in self.vertices:
            self.agregar_vertice(origen)
        if destino not in self.vertices:
            self.agregar_vertice(destino)
        self.vertices[origen]['ady'][destino] = peso
        if self.tipo == no_dirigido:
            self.vertices[destino]['ady'][origen] = peso

    def eliminar_arista(self,origen,destino):
        if self.tipo == no_dirigido:
            self.vertices[destino]['ady'].pop(origen)
        return self.vertices[origen]['ady'].pop(destino)

    def vertice_random(self):
        for i in self.vertices:
            return i

    def pertenece(self,vertice):
        return vertice in self.vertices

    def peso(self,origen,destino):
        if destino not in self.vertices[origen]['ady']: return None
        return self.vertices[origen]['ady'][destino]

    def vertices(self):
        return self.vertices.keys()

    def adyacentes(self,vertice,peso = None):
        if peso != None: return self.vertices[vertice]['ady'].items()
        return self.vertices[vertice]['ady'].keys()
