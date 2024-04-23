import geopandas as gpd
import matplotlib.pyplot as plt
from graph_builder import GraphBuilder
from greyWolfOptimizer import GreyWolfOptimizer

# Nombre del archivo TopoJSON que contiene los datos de los municipios
nombre_archivo = 'data/municipios.json'

# Cargar el archivo TopoJSON como un GeoDataFrame
gdf = gpd.read_file(nombre_archivo)

# Filtrar las geometrías correspondientes a un departamento específico (ej. Chocó)
departamento = 'CHOCO'
municipios_choco = gdf[gdf['dpt'] == departamento]

# Crear instancia de GraphBuilder y construir el grafo con un umbral de distancia
graph_builder = GraphBuilder(municipios_choco)
umbral_distancia = 100  # Definir el umbral de distancia en kilómetros
nodos, conexiones = graph_builder.construir_grafo(umbral_distancia)

# Crear instancia de GreyWolfOptimizer
gwo = GreyWolfOptimizer(graph_builder)

# Definir nodo de partida y nodo de llegada
nodo_partida = 'QUIBDO'
nodo_llegada = 'ACANDI'

# Optimizar la ruta utilizando Grey Wolf Optimization
mejor_ruta = gwo.optimizar_ruta_gwo(nodo_partida, nodo_llegada)

# Calcular el costo total, distancia recorrida y medios de transporte utilizados
costo_total, distancia_recorrida, cambios_transporte = gwo.calcular_costo_ruta(mejor_ruta)

# Mostrar información detallada por consola
print(f"Mejor Ruta: {mejor_ruta}")
print(f"Costo Total: {costo_total}")
print(f"Distancia Recorrida (km): {distancia_recorrida:.2f} km")

if cambios_transporte:
    print("Detalles de los Medios de Transporte Utilizados:")
    for cambio in cambios_transporte:
        nodo = cambio[0]
        transporte = cambio[1]
        print(f"Desde {nodo} en {transporte}")

# Visualizar los municipios y conexiones en un mapa
fig, ax = plt.subplots(figsize=(10, 10))
municipios_choco.plot(ax=ax, edgecolor='black', alpha=0.5)

# Agregar etiquetas de nombres de municipios
for x, y, label in zip(municipios_choco.geometry.centroid.x,
                        municipios_choco.geometry.centroid.y,
                        municipios_choco['name']):
    ax.text(x, y, label, fontsize=8, ha='center', va='center', color='black')

# Agregar líneas para representar las conexiones entre municipios
for conexion in conexiones:
    municipio1 = conexion[0]
    municipio2 = conexion[1]
    geom1 = municipios_choco[municipios_choco['name'] == municipio1].geometry.values[0]
    geom2 = municipios_choco[municipios_choco['name'] == municipio2].geometry.values[0]
    x_coords = [geom1.centroid.x, geom2.centroid.x]
    y_coords = [geom1.centroid.y, geom2.centroid.y]
    ax.plot(x_coords, y_coords, 'b-', alpha=0.7)  # Línea azul para las conexiones

# Mostrar el mapa con todas las rutas disponibles
plt.title('Municipios y Conexiones en Chocó', fontsize=16)
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.show()

# Visualizar solo la mejor ruta encontrada en un mapa
fig, ax = plt.subplots(figsize=(10, 10))
municipios_choco.plot(ax=ax, edgecolor='black', alpha=0.5)

# Agregar líneas para representar la mejor ruta encontrada
for i in range(len(mejor_ruta) - 1):
    nodo_actual = mejor_ruta[i]
    nodo_siguiente = mejor_ruta[i + 1]
    geom1 = municipios_choco[municipios_choco['name'] == nodo_actual].geometry.values[0]
    geom2 = municipios_choco[municipios_choco['name'] == nodo_siguiente].geometry.values[0]
    x_coords = [geom1.centroid.x, geom2.centroid.x]
    y_coords = [geom1.centroid.y, geom2.centroid.y]
    ax.plot(x_coords, y_coords, 'r-', alpha=0.7)  # Línea roja para la mejor ruta

# Mostrar el mapa con la mejor ruta encontrada
plt.title('Mejor Ruta en Chocó', fontsize=16)
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.show()

