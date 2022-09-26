import math
from matplotlib import pyplot as plt

class Vertice:
    def __init__(self, valor, x, y):
        self.__valor = valor
        self.__x = x
        self.__y = y
        self.__arestas = set()
    
    def getValor(self):
        return self.__valor
    def setValor(self, valor):
        self.__valor = valor

    def getX(self):
        return self.__x
    def setX(self, x):
        self.__x = x

    def getY(self):
        return self.__y
    def setY(self, y):
        self.__y = y
        
    def getArestas(self):
        return self.__arestas

    def adicionarAresta(self, aresta):
        self.__arestas.add(aresta)


class Aresta:
    def __init__(self, vOrigem, vDestino):
        self.__vOrigem = vOrigem
        self.__vDestino = vDestino
        self.__vOrigem.adicionarAresta(self)
        self.__vDestino.adicionarAresta(self)
        
    def getvOrigem(self):
        return self.__vOrigem
    def getvDestino(self):
        return self.__vDestino

    def getTamanho(self):
        return math.sqrt((math.pow(self.__vDestino.getX() - self.__vOrigem.getX(), 2)) + (math.pow(self.__vDestino.getY() - self.__vOrigem.getY(), 2)))


class Grafo:
    def __init__(self):
        self.__vertices = set()
        self.__arestas  = set()
        
    def setArestas(self, arestas):
        self.__arestas = arestas
    def getArestas(self):
        return self.__arestas

    def setVertices(self, vertices):
        self.__vertices = vertices
    def getVertices(self):
        return self.__vertices 

    def setTodasArestas(self):
        for verticeOrigem in self.getVertices():
            for verticeDestino in self.getVertices():
                grafo.setArestas(Aresta(verticeOrigem, verticeDestino))

    def verTodosOsVerticesComTodasAsArestas(self):
        for v in self.getVertices():
            print(f"Nome do vertice {v.getValor()}, Posicao do vertice X={v.getX()} Y={v.getY()}")
            print("Arestas...")
            for a in v.getArestas():
                print(f"Vertice de origem {a.getvOrigem().getValor()}, Vertice de destino {a.getvDestino().getValor()}, Distancia {a.getTamanho()}")
            print("")

    def verMatplotlib(self):
        x = []
        y = []

        for vxy in self.getVertices():
            x.append(vxy.getX())
            y.append(vxy.getY())

        plt.scatter(x,y)
        plt.show()


    def ACS(self, tamanhoProblema, m, p, b, o, q0):
        pOtimo = criarSolucaoEuristica(tamanhoProblema)
        pOtimoCusto = custo(sh)
        feromonioInicial = 1 / (tamanhoProblema * pOtimoCusto)
        feromonio = iniciarFeromonio(feromonioInicial)

        while condicaoDeParada():
            for i in range(1, m):
                si = criarSolucao(feromonio,tamanhoProblema,B,q0)
                siCusto = custo(si)
                if siCusto <= pOtimoCusto:
                    pOtimoCusto = siCusto
                    pOtimo = si
                atualizarFeromonioLocal(feromonio,si,siCusto, o)
            atualizarFeromonioGlobal(feromonio,pOtimo,pOtimoCusto,p)

        return pOtimo



a = Vertice('A', 8, 2)
b = Vertice('B', 0, 4)
c = Vertice('C', -1, 6)
d = Vertice('D', 2, -1)
e = Vertice('E', 4, -2)
f = Vertice('F', 6, 0.5)
g = Vertice('G', 3, 0)
h = Vertice('H', 10, 3.7)
i = Vertice('I', 2.5, 1.8)
j = Vertice('J', -5, 1)
k = Vertice('K', 7, 0)
l = Vertice('L', 9, 4)
m = Vertice('M', 11, 3)
n = Vertice('N', 13, 2)


G = Grafo()
G.setVertices({a,b,c,d,e,f,g,h,i,j,k,l,m,n})
G.setTodasArestas()







