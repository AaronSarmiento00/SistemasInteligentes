import csv
import sys
from Model.grafo import Grafo
from Model.vereda import Vereda
from Model.gwo import grey_wolf_optimizer

# Aumentar el límite del tamaño de los campos
csv.field_size_limit(sys.maxsize)

def cargar_datos(ruta_archivo):
    """
    Carga los datos del archivo CSV y crea el grafo de veredas.
    
    Parámetros:
    -----------
    ruta_archivo : str
        Ruta del archivo CSV.
    
    Retorno:
    --------
    Grafo
        Grafo de veredas cargado con los datos del archivo.
    """
    grafo = Grafo()
    nodos_a_excluir = {26041, 25512, 25504, 25517, 25505, 25501, 25534}  # Nodos problemáticos
    
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo, delimiter=';')
        
        veredas = []
        
        for fila in lector_csv:
            vereda_id = int(fila['OBJECTID'])  # Asegúrate de que el ID sea un entero
            if vereda_id in nodos_a_excluir:
                continue  # Saltar nodos problemáticos
            
            nombre = fila['NOMBRE_VER']
            lat, lon = map(float, fila['geo_point_2d'].split(','))
            vereda = Vereda(vereda_id, nombre, (lat, lon))
            veredas.append(vereda)
            grafo.agregar_nodo(vereda)
        
        for i in range(len(veredas) - 1):
            lat1, lon1 = veredas[i].coordenadas
            lat2, lon2 = veredas[i+1].coordenadas
            coord1 = (lat1, lon1)
            coord2 = (lat2, lon2)
            distancia = Grafo.calcular_distancia(coord1, coord2)
            grafo.agregar_arista(veredas[i].id, veredas[i+1].id, distancia)
            grafo.agregar_arista(veredas[i+1].id, veredas[i].id, distancia)  # Agregar arista en sentido inverso

    # Verifica que todos los nodos tengan vecinos
    nodos_sin_vecinos = [nodo for nodo in grafo.nodos if nodo not in grafo.aristas or not grafo.aristas[nodo]]
    if nodos_sin_vecinos:
        print(f"Nodos sin vecinos: {nodos_sin_vecinos}")

    return grafo

def encontrar_ruta_optima(grafo, inicio, fin):
    """
    Encuentra la ruta más óptima entre dos nodos usando el algoritmo GWO.
    
    Parámetros:
    -----------
    grafo : Grafo
        Grafo de veredas.
    inicio : int
        Nodo inicial.
    fin : int
        Nodo final.
    
    Retorno:
    --------
    list
        Lista de nodos que representa la ruta más óptima.
    """
    def funcion_costo(camino):
        return sum(grafo.aristas[camino[i]][camino[i+1]] for i in range(len(camino) - 1))
    
    mejor_camino = grey_wolf_optimizer(funcion_costo, grafo, inicio, fin)
    
    return mejor_camino
