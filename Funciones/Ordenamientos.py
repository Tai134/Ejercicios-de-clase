def ordenamiento_burbuja(listado):
    n = len(listado)
    for i in range(n-1):
        for j in range(n-i-1):
            if listado[j] > listado[j+1]:
                listado[j], listado[j+1] = listado[j+1], listado[j]

    return listado

# print(ordenamiento_burbuja([43, 54, 3, 34, 22, 10, 9])) #Pasar por pythontutor

def ordenamiento_burbuja1(listado):
    n = len(listado)
    for i in range(n-1):
        for j in range(i+1, n):
            if listado[j] < listado[i]: 
                aux = listado[i]
                listado[i] = listado[j]
                listado[j] = aux

    return listado

# print(ordenamiento_burbuja1([43, 54, 3, 34, 22, 10, 9]))

legajos = [4, 2, 5, 3]
nombres = ["Ana Lopez", "Pedro Gomez", "Jose Perez", "Marta Sanchez"]

def ordenamiento_arr_paral(legajo, nombre):
    n = len(legajo)

    for i in range(n-1):
        for j in range(i+1, n):
            if legajo[j] < legajo[i]:
                aux_legajo = legajo[i]
                legajo[i] = legajo[j]
                legajo[j] = aux_legajo

                aux_nombre = nombre[i]
                nombre[i] = nombre[j]
                nombre[j] = aux_nombre

    return legajo, nombre

ordenar = ordenamiento_arr_paral(legajos, nombres)
print(ordenar)