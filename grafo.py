import random

no_dirigido = 1

class Grafo():
    def __init__(self,tipo = no_dirigido,vertices = None,aristas = None):
        self.vertices = {}
        self.tipo = tipo
        if vertices != None:
            for i in vertices:
                self.vertices[i] = {}
        if aristas != None:
            for j in aristas:
                if len(j) == 2:
                    self.agregar_arista(j[0],j[1])
                else:
                    self.agregar_arista(j[0],j[1],j[2])
        '''vertices y aristas son listas con todos las aristas y vertices 
        del grafo para crear un grafo con elementos ya insertados'''

    def destruir(self):
        self.vertices.clear()

    def agregar_vertice(self,vertice):
        if not self.vertices.__contains__(vertice):
            self.vertices[vertice] = {}

    def eliminar_vertice(self,vertice):
        if not self.vertices.__contains__(vertice): return None
        if self.tipo == no_dirigido:
            for i in self.vertices[vertice].keys():
                self.vertices[i].pop(vertice)
        return self.vertices.pop(vertice,None)

    def agregar_arista(self,origen,destino,peso = None):
        if origen not in self.vertices or destino not in self.vertices: return None
        self.vertices[origen][destino] = peso
        if self.tipo == no_dirigido:
            self.vertices[destino][origen] = peso

    def eliminar_arista(self,origen,destino):
        if self.tipo == no_dirigido:
            self.vertices[destino].pop(origen)
        return self.vertices[origen].pop(destino)

    def vertice_random(self):
        for i in self.vertices:
            return i

    def pertenece(self,vertice):
        return self.vertices.__contains__(vertice)

    def peso(self,origen,destino):
        if not self.vertices[origen].__contains__(destino): return None
        return self.vertices[origen][destino]

    def adyacentes(self,vertice,peso = None):
        """ady = []
        for i in self.vertices[vertice].keys:
            ady.append(i)
        return ady """
        if peso != None: return self.vertices[vertice].items()
        return self.vertices[vertice].keys()

    def iterar(self):
        #Puede que no vaya aca, nose.
        return