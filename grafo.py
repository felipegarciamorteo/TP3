import random

no_dirigido = 1

class Grafo():
    def __init__(self,vertices = None,aristas = None,tipo = no_dirigido):
        self.vertices = {}
        if vertices != None:
            for i in vertices:
                self.vertices[i] = {}
                #vertices es una lista con todos los vertices del grafo
        #self.matriz = [][]
        self.tipo = tipo

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
        self.vertices[origen][destino] = peso
        if self.tipo == no_dirigido:
            self.vertices[destino][origen] = peso

    def eliminar_arista(self,origen,destino):
        if self.tipo == no_dirigido:
            self.vertices[destino].pop(origen)
        return self.vertices[origen].pop(destino)

    def vertice_random(self):
        return random.choice(self.vertices)

    def pertenece(self,vertice):
        return self.vertices.__contains__(vertice)

    def peso(self,origen,destino):
        if not self.vertices[origen].__contains__(destino): return None
        return self.vertices[origen][destino]

    def adyacentes(self,vertice):
        """ady = []
        for i in self.vertices[vertice].keys:
            ady.append(i)
        return ady """
        return self.vertices[vertice].items()

    def iterar(self):
        #Puede que no vaya aca, nose.
        return