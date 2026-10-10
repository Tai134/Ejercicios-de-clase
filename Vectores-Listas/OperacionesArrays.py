#Clase 06/10

cadena = 'Hola Mundo!'
cadena_uno = 'Hola'
cadena_dos = 'Mundo!'

print(type(cadena))

print(cadena[3])

### Slicing ###
print(cadena[1:3])

### LEN ###
print(f"La cantidad de caracteres que tiene la cadena es: {len(cadena)}")

### Concatenar ###
print(cadena_uno + cadena_dos)

### Repeticion de cadena ###
print(cadena_uno * 3)

### Comparacion de cadenas ###
if cadena_uno == cadena_dos:
    print('Las cadenas son iguales')
else:
    print('Las cadenas son diferentes')

if cadena_uno > cadena_dos:
    print('Cadena Uno es mayor')
else:
    print('Cadena Dos es mayor')

### Buscar en la cadena ###

buscar = input('Ingrese un caracter: ')

for caracter in cadena:
    if caracter == buscar:
        print('Caracter encontrado')
        break


### Buscar mas especifico ###
bandera = False
buscar2 = input('Ingrese un caracter: ')
for caracter in cadena:
    if caracter == buscar2:
        print('Caracter encontrado')
        bandera = True
        break

if bandera == False:
    print('Caracter no encontrado')


### Son inmutables ###
# array = 'Zacarias'
# array[2] = 'k' ---> Rompe porque no se pueden cambiar cambiar/mutar


### Normalizacion ###
array1 = 'Cadena'
print(array1 == 'cadena')
#convertir --> array1 = 'Cadena' -> array1 = 'cadena'

### Arrays Paralelas ###
apellidos = ['Perez', 'Gomez', 'Rodriguez']
nombre = ['Alba', 'Pedro', 'Ramon']
legajo = [87, 83, 82]

for i in range(len(apellidos)):
    print(f"{legajo[i]} {nombre[i]} {apellidos[i]}")

#--------------------------------------------------------------------------------------------#

descripcion = ["Maza", "Pinza", "Tenaza"]
precio_compra = [100, 200, 300]
codigo = [1, 2, 3]
precio_venta = [0, 0, 0]

print("\t\t\tLISTADO DE PRODUCTOS")
print("COD\tDESCRIPCION\t\tP.COMPRA")
for i in range(len(codigo)):
    print(f"{codigo[i]}\t{descripcion[i]}\t\t\t{precio_compra[i]}")
    
for i in range(len(codigo)):
    precio_venta[i] = precio_compra[i] * 1.3
    
print("\n\t\t\tLISTADO DE PRODUCTOS CON PRECIO DE VENTA")
print("COD\tDESCRIPCION\t\tP.COMPRA\t\tP.VENTA")
for i in range(len(codigo)):
    print(f"{codigo[i]}\t{descripcion[i]}\t\t\t{precio_compra[i]}\t\t\t{precio_venta[i]}")