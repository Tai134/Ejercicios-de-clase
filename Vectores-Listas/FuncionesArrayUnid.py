def crear_array(cantidad:int)->list:
    '''
    Esta funcíon devolvera un array con la cantidad de elementos indicada en el parametro

    '''
    array = [0] * cantidad # Es vacia y multiplica por la cantidad de numeros que le doy entonces toma ese valor como cantidad de items
    return array

# new_array = crear_array(6)
# for elemento in new_array:
#     print(elemento)


def poblar_array(numero:int):
    
    lista = crear_array(numero)
    
    for i in range(len(lista)):
        lista[i] = (i+1)
        
    return lista
        
# mi_lista = poblar_array(5)
# for elemento in mi_lista:
#     print(elemento)

def promedio_array(numero:int):
    
    lista = crear_array(numero)
    suma = 0
    for i in range(len(lista)):
        num = int(input("Ingresa un número: "))
        lista[i] += num
        suma += num
    
    prom = suma / numero
    return prom

# promedio = promedio_array(3)
# print(promedio)

def promedio_positivos(numero:int):
    
    lista = crear_array(numero)
    suma = 0
    positivos = 0
    for i in range(len(lista)):
        num = int(input("Ingresa un número: "))
        lista[i] += num
        if num > 0:    
            suma += num
            positivos += 1

    if positivos == 0:
        return 0
    
    prom = suma / positivos # -> En caso de que solo se cuenten los positivos el divisor
    #prom = suma / numero
    return prom


# promiedo = promedio_positivos(5)
# if promiedo == 0:
#     print("El promedio es 0")
# else:
#     print(f"El promedio es: {round(promiedo, 2)}")

def producto_array(numero:int):
    lista = crear_array(numero)
    multiplicacion = 1
    for i in range(len(lista)):
        num = int(input("Ingresa un número: "))
        lista[i] += num
        multiplicacion *= num

    return multiplicacion

# producto = producto_array(6)
# print(producto)

def obtener_maximo(lista:list)->int:
    for i in range(len(lista)):
        if i == 0:
            indice_maximo = i
            maximo = lista[i]
        if lista[i] > maximo:
            indice_maximo = i
            maximo = lista[i]
        
    return indice_maximo

# print(obtener_maximo([3,5,7,4]))

def obtenerymostrar_maximo(lista:list)->int:
    lista_maximos = []  
    for i in range(len(lista)):
        if i == 0:
            indice_maximo = i
            maximo = lista[i]
        elif lista[i] > maximo:
            indice_maximo = [i]
            maximo = lista[i]
            lista_maximos = [i]
        elif lista[i] == maximo:
            lista_maximos += [i]
    print(maximo)
    return lista_maximos

#print(obtenerymostrar_maximo([3,5,7,7,4]))

lista_nombres = ['Taiel','Victoria','Bruno','Emi','Ema','Bruno','Lauti']
nombre_antiguo = 'Bruno'
nombre_nuevo = 'Agus'

def reemplazar_nombres(nombre:list)->list:
    cont_reemplazos = 0
    for i in range(len(nombre)):
        if nombre[i] == nombre_antiguo:
            nombre[i] = nombre_nuevo
            cont_reemplazos += 1

    print(lista_nombres)
    return cont_reemplazos

# test = reemplazar_nombres(lista_nombres)
# print(test)

array_1 = ['a','b','r','c','d','e']
array_2 = ['t','d','r','y','a','x']

def interseccion_array (arr_1:list,arr_2:list)->list:
    interseccion = []
    for i in range(len(arr_1)):
        for j in range(len(arr_2)):
            if arr_1[i] == arr_2[j]:
                interseccion += arr_2[j]

    return interseccion

# inter = interseccion_array(array_1,array_2)
# print(inter)

def union_array (arr_1:list,arr_2:list)->list:
    union = []
    for i in range(len(arr_1)):
        repetidas = False
        for j in range(len(union)):
            if arr_1[i] == union[j]:
                repetidas = True
                break
        
        if repetidas == False:
            union += arr_1[i]

    for i in range(len(arr_2)):
        repetido = False
        for j in range(len(union)):
            if arr_2[i] == union[j]:
                repetido = True
                break
                
        if repetido == False:
            union += [arr_2[i]]
    
    return union

# uni = union_array(array_1,array_2)
# print(uni)


# Hacer punto 11 sobre esta funcion

def diff_array (arr_1:list,arr_2:list)->list:
    diff = []
    for i in range(len(arr_1)):
        repetidas = False
        for j in range(len(arr_2)):
            if arr_1[i] == arr_2[j]:
                repetidas = True
                break
        
        if repetidas == False:
            diff += arr_1[i]
     
    return diff

diferencias = diff_array(array_1, array_2)
print(diferencias)