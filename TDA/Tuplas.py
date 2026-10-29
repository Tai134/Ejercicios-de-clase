# Son inmutables
# lista = tuple([1, 'hola', 3.67])
# print(type(lista))
# print(lista[1])
# lista[1] = 'Chau'

# Desempaquetado
mi_tupla = (5, 2, 4, 3)
mi_lista = [5, 2, 4, 3]
print(type(mi_tupla))
print(type(mi_lista))

mi_tupla1 = ('Juan', 'Perez', 30)
nombre, apellido, edad = mi_tupla1

print(nombre)
print(apellido)
print(edad)

mi_lista.sort()
print(mi_lista)

mi_lista.sort(reverse=True)
print(mi_lista)