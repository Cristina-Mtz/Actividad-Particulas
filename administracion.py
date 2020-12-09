from particula import Particula
from pprint import pprint
from pprint import pformat
import json


class Administracion:
    def __init__(self):
        self.__particulas = [] 
        self.grafos = dict()
        self.grafos = {}
       

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

    def __str__(self):
        return "".join(
           str(particula) + '\n' for particula in self.__particulas
        )

    def __len__(self):
        return len(self.__particulas)

    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration


    def guardar(self,ubicacion):
        try:   
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict()for particula in self.__particulas]
                print(lista)
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0

    def grafo(self):
        for particula in self.__particulas:
            origen = (particula.origen_x,particula.origen_y)
            destino = (particula.destino_x, particula.destino_y)
            if origen in self.grafos:
                if destino in self.grafos[origen]:
                    pass 
                else:
                    self.grafos[origen].append((destino,round(particula.distancia,2)))
            else:
                self.grafos[origen] = [(destino,round(particula.distancia,2))]

            if destino in self.grafos:
                if origen in self.grafos[destino]:
                    pass
                else:
                    self.grafos[destino].append((origen,round(particula.distancia,2)))
            else:
                self.grafos[destino] = [(origen,round(particula.distancia,2))]
        str = pformat(self.grafos, width=40) 
        return(str)

    def profundidad(self, o_x, o_y):
        vertice = (o_x, o_y)
        visitados = []
        pila = []
        recorrido = []
        visitados.append(vertice)
        pila.append(vertice)

        while len(pila) > 0:
            vertice = pila[(len(pila)-1)]
            recorrido.append(vertice)
            pila.pop()

            for adya in self.grafos[vertice]:
                if adya[0] in visitados:
                    pass
                else:
                    visitados.append(adya[0])
                    pila.append(adya[0])
        str = pformat(recorrido, width=40) 
        return str

    def amplitud (self, o_x, o_y):
        vertice = (o_x, o_y)
        visitados = []
        cola = []
        recorrido = []
        visitados.append(vertice)
        cola.append(vertice)

        while len(cola) > 0:
            vertice = cola[(len(cola)-1)]
            recorrido.append(vertice)
            cola.pop()

            for adya in self.grafos[vertice]:
                if adya[0] in visitados:
                    pass 
                else:
                    visitados.append(adya[0])
                    cola.insert(0,adya[0])
        str = pformat(recorrido, width=40) 
        return str
        

    
    
   


   


