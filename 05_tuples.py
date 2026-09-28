### Tuples ###

my_tuple = tuple() # Tupla vacía
my_other_tuple = () # Tupla vacía

my_tuple = (35, 1.77, "John", "Doe") # Tupla con elementos
my_other_tuple = (35, 24, 62, 52, 30, 17) # Tupla con elementos

print(my_tuple) # Print tupla
print(type(my_tuple)) # Tipo de dato 'tuple'

print(my_tuple[0]) # Acceso a elementos de la tupla
print(my_tuple[-1]) # Acceso a elementos de la tupla 
#print(my_tuple[4]) IndexError: indice fuera de rango solo hay 0, 1, 2, 3
#print(my_tuple[-6]) IndexError: indice fuera de rango solo hay -1, -2, -3, -4

print(my_tuple.count("John")) # Cuenta cuántas veces aparece el valor "John" en la tupla
print(my_tuple.index("John")) # Devuelve el índice de la primera aparición del valor "John" en la tupla
print(my_tuple.index("Doe")) # Devuelve el índice de la primera aparición del valor "Doe" en la tupla

#my_tuple[1] = 1.80 # TypeError: 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple  # Concatenación de tuplas
print(my_sum_tuple) # Print tupla resultante de la concatenación

print(my_sum_tuple[3:6]) # Acceso a elementos de la tupla resultante de la concatenación

my_tuple = list(my_tuple) # Conversión de tupla a lista
print(type(my_tuple)) # Tipo de dato 'list'

my_tuple[2] = "Top Salas" # Cambia el elemento en la posición 2 de la lista
my_tuple.insert(1, "Verde") # Agrega un elemento en la posición 1 de la lista
my_tuple = tuple(my_tuple) # Conversión de lista a tupla
print(my_tuple) # Print lista resultante de la conversión de tupla a lista
print(type(my_tuple)) # Tipo de dato 'tuple' 

### Las tuplas son inmutables, no se pueden agregar ni eliminar elementos de una tupla, pero se puede convertir a lista para modificarla y luego volver a convertirla a tupla. ###

#del my_tuple[2] # TypeError: 'tuple' object doesn't support item deletion

del my_tuple # Elimina la tupla
#print(my_tuple) # NameError: name 'my_tuple' is not defined