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
def depth_first_search(graph, source):
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
    print("Búsqueda en Profundidad")
    print("----------------------------------")
    if source is None or source not in graph:
        return "El node ingresado no pertenece al grafo"

    #Inicialización de variables
    path = [] # Lista para almanecnar los nodos visitados
    pathCost = 0 # Variable que almacena el costo acumulado de la ruta del árbol generado
    stack = [[source, 0, None]] # Lista de control sobre los nodos vecinos candidatos a ser visitados. Se inicializa con el nodo desde donde comenzará la búsqueda
    print("\nIniciando la búsqueda desde " + source)

    #Ciclo de control sobre los nodos del grafo
    while (len(stack) != 0):
        vectorInfo = stack.pop() # Obtenemos la información del último nodo en la lista (Nombre y Distancia)

        if vectorInfo[0] not in path: # Validamos que el nodo no haya sido visitado
            path.append(vectorInfo[0]) # Se agrega el nodo a la lista de visitados
            if vectorInfo[0] is not source:
                pathCost = pathCost + vectorInfo[1] # Se suma el costo de visitar a ese nodo a la variable de costo acumulado de la ruta
                print('\nVisitando a {child} desde {parent}'.format(child=vectorInfo[0], parent=vectorInfo[2]))
                print("Costo Acumulado de Ruta: ", pathCost)

        if vectorInfo[0] not in graph: # Si el nodo no está en el grafo, seguimos adelante
            continue
        for neighbor in graph[vectorInfo[0]]: # Para el nodo en análisis, se obtienen sus vecinos, los cuáles podrían ser nodos a ser visitados.
            if len(neighbor) > 0:
                neighbor.append(vectorInfo[0])
                stack.append(neighbor)
    return " ".join(path)

#Invocando ejecución de Búsqueda en Profundidad
DFS_path = depth_first_search(directions_graph, "UAI")
print("\nRuta obtenida con Búsqueda en Profundidad: " + DFS_path)