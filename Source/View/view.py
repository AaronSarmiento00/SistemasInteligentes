# View/view.py
"""
Visualización del grafo de veredas.
"""

import matplotlib.pyplot as plt

def visualizar_grafo(grafo):
    """
    Visualiza el grafo de veredas usando Matplotlib.
    
    Parámetros:
    -----------
    grafo : Grafo
        Grafo de veredas a visualizar.
    """
    plt.figure(figsize=(10, 10))

    for nodo, adyacentes in grafo.aristas.items():
        for adyacente, distancia in adyacentes.items():
            plt.plot(
                [grafo.nodos[nodo]['coordenadas'][1], grafo.nodos[adyacente]['coordenadas'][1]],
                [grafo.nodos[nodo]['coordenadas'][0], grafo.nodos[adyacente]['coordenadas'][0]],
                'k-', lw=0.5
            )

    for nodo, datos in grafo.nodos.items():
        plt.plot(datos['coordenadas'][1], datos['coordenadas'][0], 'ro')
        plt.text(
            datos['coordenadas'][1], datos['coordenadas'][0], nodo,
            fontsize=8, ha='right'
        )

    plt.xlabel('Longitud')
    plt.ylabel('Latitud')
    plt.title('Grafo de Veredas')

    # Leyenda personalizada para evitar la superposición en el mapa
    etiquetas = [nodo for nodo in grafo.nodos]
    plt.legend(etiquetas, loc='upper left', fontsize='small', bbox_to_anchor=(1, 1))

    plt.grid(True)
    plt.show()
