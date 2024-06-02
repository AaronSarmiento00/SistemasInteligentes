import random

def grey_wolf_optimizer(funcion_costo, grafo, inicio, fin, max_iter=100, num_lobos=5):
    """
    Implementación del algoritmo de Grey Wolf Optimizer para encontrar la ruta óptima en un grafo.
    
    Parámetros:
    -----------
    funcion_costo : function
        Función de costo para evaluar los caminos.
    grafo : Grafo
        Grafo de veredas.
    inicio : int
        Nodo inicial.
    fin : int
        Nodo final.
    max_iter : int, opcional
        Número máximo de iteraciones (por defecto 100).
    num_lobos : int, opcional
        Número de lobos en la población (por defecto 5).
    
    Retorno:
    --------
    list
        Lista de nodos que representa la ruta más óptima.
    """
    
    def inicializar_lobos():
        """
        Inicializa la población de lobos con caminos aleatorios.
        
        Retorno:
        --------
        list
            Lista de caminos aleatorios.
        """
        lobos = []
        intentos = 0
        while len(lobos) < num_lobos and intentos < num_lobos * 10:
            camino = generar_camino_aleatorio(grafo, inicio, fin)
            if camino:
                lobos.append(camino)
            else:
                print(f"Error: No se pudo generar un camino aleatorio desde {inicio} hasta {fin}.")
            intentos += 1
        return lobos

    def generar_camino_aleatorio(grafo, inicio, fin):
        """
        Genera un camino aleatorio desde inicio hasta fin.
        
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
            Lista de nodos que representa el camino aleatorio.
        """
        camino = [inicio]
        actual = inicio
        while actual != fin:
            vecinos = list(grafo.aristas[actual].keys())
            if not vecinos:
                print(f"Error: El nodo {actual} no tiene vecinos, camino roto.")
                return None  # No hay camino posible
            actual = random.choice(vecinos)
            if actual in camino:  # Evitar ciclos
                print(f"Advertencia: Se ha detectado un ciclo en el nodo {actual}.")
                return None
            camino.append(actual)
        return camino

    def actualizar_posiciones(lobos, a, A, C):
        """
        Actualiza las posiciones de los lobos en función de las reglas de GWO.
        
        Parámetros:
        -----------
        lobos : list
            Lista de caminos de los lobos.
        a : float
            Coeficiente de disminución.
        A : list
            Vector de coeficientes A.
        C : list
            Vector de coeficientes C.
        
        Retorno:
        --------
        list
            Lista de caminos actualizados.
        """
        for i in range(len(lobos)):
            for j in range(len(lobos[i])):
                D_alpha = abs(C[0] * alfa[j] - lobos[i][j])
                D_beta = abs(C[1] * beta[j] - lobos[i][j])
                D_delta = abs(C[2] * delta[j] - lobos[i][j])

                X1 = alfa[j] - A[0] * D_alpha
                X2 = beta[j] - A[1] * D_beta
                X3 = delta[j] - A[2] * D_delta

                lobos[i][j] = (X1 + X2 + X3) / 3
        return lobos

    # Inicialización
    lobos = inicializar_lobos()
    
    if not lobos:
        raise ValueError("No se pudo inicializar la población de lobos")

    alfa, beta, delta = sorted(lobos, key=funcion_costo)[:3]

    for iter in range(max_iter):
        a = 2 - iter * (2 / max_iter)  # a disminuye linealmente de 2 a 0

        A = [2 * a * random.random() - a for _ in range(3)]
        C = [2 * random.random() for _ in range(3)]

        lobos = actualizar_posiciones(lobos, a, A, C)

        # Actualizar alfa, beta y delta
        alfa, beta, delta = sorted(lobos, key=funcion_costo)[:3]
    
    return alfa

