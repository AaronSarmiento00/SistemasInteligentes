# mainfile.py

"""
Archivo principal para ejecutar el programa.
"""

from Controller.controller import cargar_datos, encontrar_ruta_optima
from View.view import visualizar_grafo

def main():
    """
    Función principal del programa.
    """
    ruta_archivo = 'DataSets/tabla_veredas.csv'
    grafo = cargar_datos(ruta_archivo)
    
    inicio = 24535  # ID de nodo de inicio, ajustar según sea necesario
    fin = 25396  # ID de nodo de fin, ajustar según sea necesario
    
    if inicio not in grafo.nodos or fin not in grafo.nodos:
        print(f"El nodo de inicio ({inicio}) o el nodo de fin ({fin}) no existen en el grafo.")
        return
    
    # Verificar si los nodos de inicio y fin tienen vecinos
    if not grafo.aristas.get(inicio):
        print(f"El nodo de inicio ({inicio}) no tiene vecinos.")
        return

    if not grafo.aristas.get(fin):
        print(f"El nodo de fin ({fin}) no tiene vecinos.")
        return
    
    ruta_optima = encontrar_ruta_optima(grafo, inicio, fin)
    
    print(f'Ruta óptima de {inicio} a {fin}: {ruta_optima}')
    
    visualizar_grafo(grafo)

if __name__ == "__main__":
    main()
