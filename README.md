# uai-mia-search_tree
Técnicas de Búsquedas y Heurísticas - Implementación en Python de Algoritmos de Búsqueda en Anchura y Búsqueda en Profundidad


## Psheudocódigo Búsqueda en Profundidad (Depth First Search)

ALGORITMO BusquedaEnProfundidad(CARACTER grafo[][], CARACTER nodoInicio)

VAR 

    CARACTER ruta[];
    ENTERO costoRuta;
    CARACTER nodosVecinos[][] <- [0][nodoInicio, 0, NULO]; // Lista Doble-> Primer Nivel: Posibles nodos a visitar - Segundo Nivel: Información de nodo (0=Nombre, 1=Distancia, 2=Padre)

INICIO

    MIENTRAS( LONGITUD(nodosVecinos) > 0) HACER
        CARACTER informacionNodo[] <- nodosVecinos[(LONGITUD(nodosVecinos)-1)] // Obtenemos último registro de la lista (0=Nombre, 1=Distancia, 2=Padre)

        // EJECUCIÓN DE VISITAS
        SI informacionNodo[0] NO PERTENCE A ruta // Validamos que no se haya visitado el nodo
            AGREGAR(ruta) <- informacionNodo[0] // Agregamos el nombre del nodo a la lista de nodos visitados
            costoRuta <- costoRuta + informacionNodo[1]
        FIN SI

        // OBTENCIÓN DE CANDIDATOS A SER VISITADOS
        PARA vecino EN grafo->(informacionNodo[0]) // Obtenermos los vecinos del nodo en análisis
            AGREGAR(vecino) <- informacionNodo[0] // Se agrega el dato del padre
            nodosVecinos <- vecino // Agregamos este vecino a nodos que posiblemente serán visitados
        FIN PARA 

    FIN MIENTRAS

    RETORNAR ruta

FIN
