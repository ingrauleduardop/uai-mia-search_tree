# Estructura 'Directory' que nos servirá para almacenar la representación del grafo de vectores con ubicaciones de los profesores y sus distancias desde vector UAI
directions_graph = {
    'UAI': [['P1', 253], ['P2', 100], ['P3', 120]],
    'P1': [['P2', 76], ['P4', 198], ['P6', 345]],
    'P2': [['P3', 79], ['P4', 114]],
    'P3': [['P4', 123], ['P5', 115]],
    'P4': [['P5', 97], ['P6', 265], ['P7', 127], ['P8', 179]],
    'P5': [['P8', 99]],
    'P6': [['P7', 143], ['P12', 378]],
    'P7': [['P8', 87], ['P9', 92]],
    'P8': [['P9', 159], ['P10', 100], ['P11', 113]],
    'P9': [['P12', 56], ['P13', 71]],
    'P10': [['P13', 54], ['P14', 87]],
    'P11': [['P14', 134]],
    'P12': [['P15', 77]],
    'P13': [['P14', 45], ['P15', 65]],
    'P14': [['P15', 69]],
    'P15': []
}
def breadth_first_search(graph, source):
    """
    Implementación de Búsqueda en Profundidad (Depth First Search)

    Parameters:
    ----------
        :param graph (Dictionary): Grafo donde se realizará la búsqueda
        :param source (String): Nodo desde el cuál se comenzará la búsqueda
    Returns:
    --------
        :return: Lista con nodos en orden en el que fueron visitados
     """
    print("\n\n----------------------------------")
    print("Búsqueda en Anchura")
    print("----------------------------------")

    # Declaración de variable
    path = []  # Lista para nodos que se visitan.
    pathCost = 0  # Variable que almacena el costo acumulado de la ruta del árbol generado
    queue = []  # Lista de control de nodos que son candidatos a ser visitados

    # Inicialización
    path.append(source) # Se inicia con el ingreso del nodo desde donde se comienza la búsqueda
    queue.append(source) # Se inicia con el ingreso del nodo desde donde se comienza la búsqueda

    print("\nIniciando la búsqueda desde " + source)

    # Ciclo para visitar los nodos del grafo
    while queue:
        m = queue.pop(0) # Obtenemos la información del primer nodo en la lista

        # Ciclo para visitar los vecinos del nodo en análisis
        for neighbour in graph[m]:
            if neighbour[0] not in path: # Validamos que no hayan sido visitados previamente desde otro nodo
                print('\nVisitando a {child} desde {parent}'.format(child=neighbour[0], parent=m))
                pathCost = pathCost + neighbour[1]  # Se suma el costo de visitar a ese nodo a la variable de costo acumulado de la ruta
                print("Costo Acumulado de Ruta: ", pathCost)
                path.append(neighbour[0])
                queue.append(neighbour[0])
    return " ".join(path)

#Invocando ejecución de Búsqueda en Anchura
BFS_path = breadth_first_search(directions_graph, 'UAI')    # function calling
print("\nRuta obtenida con Búsqueda en Anchura: " + BFS_path)