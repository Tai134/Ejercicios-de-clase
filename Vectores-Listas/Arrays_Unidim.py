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

producto = producto_array(6)
print(producto)