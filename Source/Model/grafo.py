# Model/grafo.py
"""
Definición de la clase Grafo para representar el grafo de veredas.
"""

import math

class Grafo:
    """
    Clase que representa un grafo de veredas.
    """
    def __init__(self):
        self.nodos = {}
        self.aristas = {}

    def agregar_nodo(self, vereda):
        """
        Agrega un nodo al grafo.
        
        Parámetros:
        -----------
        vereda : Vereda
            Vereda a agregar.
        """
        if vereda.id not in self.nodos:
            self.nodos[vereda.id] = {}
            self.aristas[vereda.id] = {}

    def agregar_arista(self, id1, id2, distancia):
        """
        Agrega una arista entre dos nodos en el grafo.
        
        Parámetros:
        -----------
        id1 : int
            ID del primer nodo.
        id2 : int
            ID del segundo nodo.
        distancia : float
            Distancia entre los nodos.
        """
        if id1 in self.nodos and id2 in self.nodos:
            self.aristas[id1][id2] = distancia
            self.aristas[id2][id1] = distancia  # Si es un grafo no dirigido

    @staticmethod
    def calcular_distancia(coord1, coord2):
        """
        Calcula la distancia euclidiana entre dos coordenadas.
        
        Parámetros:
        -----------
        coord1 : tuple
            Primera coordenada (latitud, longitud).
        coord2 : tuple
            Segunda coordenada (latitud, longitud).
        
        Retorno:
        --------
        float
            Distancia euclidiana entre las dos coordenadas.
        """
        lat1, lon1 = coord1
        lat2, lon2 = coord2
        return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)
