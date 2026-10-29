# Set -> son mutables pero no tiene objetos repetidos
set = {3, 5, 9, 5, 3, 4, 3}
print(type(set))
print(set)

set_uno = {1, 2, 3}
set_dos = {3, 4, 5}

union_set = set_uno.union(set_dos)
print(union_set)

#Metodos Asociados a SETS
# .add()
# .remove()
# .discard()
# .pop()
# .clear()
# .union()
# .intersection()
# .update()

set_uno.add(4)
print(set_uno)