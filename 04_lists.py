### Listas ###

my_list = list() # Lista vacía
my_other_list = [] # Lista vacía

print(len(my_list)) # Longitud de la lista

my_list = [35, 24, 62, 52, 30, 17] # Lista con elementos]

print(my_list) # Print lista
print(len(my_list)) # Longitud de la lista

my_other_list = [35, 1.77, "John", "Doe"]

print(type(my_list)) # Tipo de dato 'list'
print(type(my_other_list)) 

print(my_other_list[0])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30)) # Cuenta cuántas veces aparece el valor 30 en la lista
print(my_other_list[1])
#print(my_other_list[4]) IndexError: indice fuera de rango solo hay 0, 1, 2, 3
#print(my_other_list[-5]) IndexError: indice fuera de rango solo hay -1, -2, -3, -4

age, height, name, surname = my_other_list # Desempaquetado de listas
print(name) 

print(my_list + my_other_list) # Concatenación de listas
#print(my_list - my_other_list) # Error: no se puede restar listas

my_other_list.append("Top Salas") # Agrega un elemento al final de la lista
print(my_other_list)

my_other_list.insert(1, "Verde") # Agrega un elemento en la posición 1 de la lista
print(my_other_list)

my_other_list[1] = "Azul" # Cambia el elemento en la posición 1 de la lista
print(my_other_list)

my_other_list.remove("Azul") # Elimina el elemento "Azul" de la lista
print(my_other_list)

my_list.remove(30) # Elimina el elemento 30 de la lista
print(my_list)

print(my_list.pop()) # Elimina el último elemento de la lista y lo devuelve
print(my_list)

my_pop_element = my_list.pop(2) # Elimina el elemento en la posición 2 de la lista y lo devuelve
print(my_pop_element)
print(my_list)

del my_list[2] # Elimina el elemento en la posición 2 de la lista
print(my_list)

my_new_list = my_list.copy() # Crea una copia de la lista
print(my_new_list)

my_list.clear() # Elimina todos los elementos de la lista
print(my_list)
print(my_new_list)

print(my_new_list.reverse()) # Invierte el orden de los elementos de la lista
print(my_new_list)

my_new_list.sort() # Ordena los elementos de la lista de menor a mayor
print(my_new_list)

print(my_new_list[1:2]) # Imprime el elemento en la posición 1 de la lista (slicing)
print(my_new_list[1:4]) # Imprime los elementos en las posiciones 1 a 3 de la lista (slicing)

my_list = "Hola mundo" # String
print(my_list) # Print string (cambio de tipo de dato de lista a string) (debilmente tipado)
print(type(my_list)) # Tipo de dato 'str'
