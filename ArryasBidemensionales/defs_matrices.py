def buscar_elemento(matriz, obejtivo):
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == obejtivo:
                elemento = matriz[i][j]
                pos1 = i
                pos2 = j
                print(f"Elemento {obejtivo} encontrado en la posición: Fila {i}, columna {j}")
                encontrado = True

            if not encontrado:
                print(f"El elemento {obejtivo} no se encontro.")

    return elemento, pos1, pos2

def buscar_en_diagonales(matriz, objetivo):

    """
    Función de búsqueda en diagonales principales y secundaria. 

    ARGS: 
    - matriz: Matriz de elementos a buscar. 
    - objetivo: Elemento a buscar.
    RETURNS:
    - elemento: valor encontrado.
    - pos1: posición del elemento encontrado en la fila. 
    - pos2: posición del elemento encontrado en la columna. 
    """
    n = len(matriz) 
    encontrado = False
    
    for i in range(n):

        """
        i = 0 y j = 0

        0,0
        1,1
        2,2
        3,3

        """
        if matriz[i][i] == objetivo:
            print(f"Encontrado en Diagonal Principal -> Posición ({i}, {i})")
            elemento = matriz[i][i]
            pos1 = i
            pos2 = i
            encontrado = True            



        """
        n = 3
        
        i = 0

        j2 = n - 1 - i
        j2 = 2 
         
        i,j2
        0,2
        1,1
        2,0
       
        """

        j2 = n - 1 - i
        if j2 != i and matriz[i][j2] == objetivo:
            print(f"Encontrado en Diagonal Secundaria -> Posición ({i}, {j2})")
            elemento = matriz[i][j2]
            pos1 = i
            pos2 = j2
            encontrado = True
            
    if not encontrado:
        print(f"El elemento {objetivo} no se encuentra en ninguna de las diagonales.")

    return elemento, pos1, pos2


def buscar_elemento_en_cantidad(matriz, objetivo):
    filas = len(matriz)
    columnas = len(matriz[0])
    encontrados = 0

    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == objetivo:
                encontrados += 1

    if encontrados == 0:
        print(f"El elemento {objetivo} no se encontró.")
    else:
        print(f"El elemento {objetivo} se encontró {encontrados} vez/veces.")

    return encontrados

