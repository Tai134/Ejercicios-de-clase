diccionario =dict([
    ('Nombre', 'Sara'),
    ('Edad', 27),
    ('Documento', 1003883),
])

# Con esta escritura tengo que aclarar que es un dict

print(type(diccionario))

diccionario1 ={
    'nombre': 'Juan',
    'edad': 21,
    'ciudad': 'Buenos Aires',
}

# El ":" hace que python detecte que es un diccionario

print(type(diccionario1))
print(diccionario1['nombre'])
print(diccionario1['edad'])
print(diccionario1['ciudad'])

# diccionario2 ={
#     'nombre', 'Juan',
#     'edad', 21,
#     'ciudad', 'Buenos Aires',
# }
# print(type(diccionario2))

#Sin el ":" lo detecta como una lista

#METODOS PARA DICCIONARIO
#.keys()
print(diccionario1.keys())
print(diccionario1.values())
print(diccionario1.items())