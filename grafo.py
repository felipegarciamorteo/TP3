import random

no_dirigido = 1
dirigido = 0
class Grafo():
    def __init__(self,tipo = no_dirigido,vertices = None,aristas = None):
        self.vertices = {}
        self.tipo = tipo
        if vertices != None:
            for i in vertices:
                self.agregar_vertice(i)
                '''self.vertices[i] = {}
                self.vertices[i]['datos'] = {}
                self.vertices[i]['ady'] = {}'''
        if aristas != None:
            for j in aristas:
                if len(j) == 2:#por si es no pesado
                    self.agregar_arista(j[0],j[1])
                else:
                    self.agregar_arista(j[0],j[1],j[2])
        '''vertices y aristas son listas con todos las aristas y vertices 
        del grafo para crear un grafo con elementos ya insertados'''

    '''def destruir(self):
        self.vertices.clear() no se si hace falta'''

    def agregar_dato(self,vertice,clave,dato):
        self.vertices[vertice]['datos'][clave] = dato

    def dato(self,vertice,clave):
        return self.vertices[vertice]['datos'][clave]

    def agregar_vertice(self,vertice):
        if vertice not in self.vertices:#not self.vertices.__contains__(vertice):
            self.vertices[vertice] = {}
            self.vertices[vertice]['ady'] = {}
            self.vertices[vertice]['datos'] = {}

    def eliminar_vertice(self,vertice):
        if vertice not in self.vertices: return None#not self.vertices.__contains__(vertice): return None
        if self.tipo == no_dirigido:
            for i in self.vertices[vertice]['ady'].keys():
                self.vertices['ady'][i].pop(vertice)
        return self.vertices.pop(vertice,None)

    def agregar_arista(self,origen,destino,peso = None):
        if origen not in self.vertices or destino not in self.vertices: return None
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
        return vertice in self.vertices#self.vertices.__contains__(vertice)

    def peso(self,origen,destino):
        if destino not in self.vertices[origen]['ady']: return None#not self.vertices[origen].__contains__(destino): return None
        return self.vertices[origen]['ady'][destino]

    def vertices(self):
        return self.vertices.keys()

    def adyacentes(self,vertice,peso = None):
        if peso != None: return self.vertices[vertice]['ady'].items()
        return self.vertices[vertice]['ady'].keys()

    
    def iterar(self):
        #Puede que no vaya aca, nose.
        return
