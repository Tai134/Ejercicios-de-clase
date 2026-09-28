from Funciones.Matematicas import *
from Funciones.Validaciones import *

### FUNCIONES RECURSIVAS ###
# def calcular_factorial (numero):
#     if numero == 0:
#         resultado = 1
#     else:
#         resultado = numero * calcular_factorial(numero - 1)

#     return resultado

# factorial = calcular_factorial(5)
# print(factorial)

# def factorial_for(numero):
#     resultado = 1
#     for i in range(1, numero + 1):
#         resultado = resultado * i
#     return resultado

# def factorial_while(numero):
#     resultado = 1
#     while numero > 0:
#         resultado = resultado * numero
#         numero = numero - 1
#     return resultado

# print(factorial_for(4))
# print(factorial_while(5))

print(es_numero('3'))
print(es_numero('T'))
print(es_numerico('4'))
print(es_numerico('Hola'))
print(es_entero('43'))
print(es_entero('-43'))
print(es_flotante('11.8'))
print(es_flotante('-11.8'))