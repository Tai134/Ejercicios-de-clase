matriz = [[1,2,3,4],
          [5,6,7,8]]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j])
    print("") #Print uno abajo del otro y espacio entre matrices


for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print("") #Print como corresponde, forma de matriz


#- - - Remplazo de elemento - - -#
#matriz1 = [[1,2,3,4],
#          [5,6,7,8]]

#print matriz1[1][0] = 5
#matriz1[1][0] = 15
#print matriz1[1][0] = 15

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz += [fila]
    
    return matriz

mi_matriz = inicializar_matriz(2, 4, 0)

for i in range(len(mi_matriz)):
    for j in range(len(mi_matriz[i])):
        print(mi_matriz[i][j], end=" ")
    print("")

def cargar_matriz_secuencialmente(matriz:list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f"Fila {i} Columna {j}: "))

cargar_matriz_secuencialmente(mi_matriz)

for i in range(len(mi_matriz)):
    for j in range(len(mi_matriz[i])):
        print(mi_matriz[i][j], end=" ")
    print("")

def cargar_matriz_aleatoriamente(matriz:list):
    seguir = "S"
    while seguir == "S":
        fila = int(input("Indice de fila: "))
        columna = int(input("Indice de columna: "))
        dato = int(input("Ingrese el número a cargar: "))
        matriz[fila][columna] = dato
        seguir = input("¿Desea seguir cargando? S/N: ")

cargar_matriz_aleatoriamente(mi_matriz)

for i in range(len(mi_matriz)):
    for j in range(len(mi_matriz[i])):
        print(mi_matriz[i][j], end=" ")
    print("")

mi_matriz1 =[[1,2,3,4],
            [5,6,7,8]]

def buscar_valor_entero(matriz:list, valor:int):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                print(f"Se encontro el número en la fila {i} columna {j}")


buscar_valor_entero(mi_matriz1, 5)