# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable)) # Tipo 'str'

my_bool_variable = True
print(my_bool_variable)

# Concatenacion de variables en un print statement
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable, "y este es el valor de:", my_int_variable) 

# Funciones del sistema
print(len(my_string_variable)) # Longitud de la variable

# Variables en una sola linea. Cuidado con abusar de esta sintaxis, puede ser confuso!
name, surname, alias, age = "John", "Doe", "Jane", 25
print("Me llamo: ", name, surname, ". Tengo ", age, " años y mi alias es: ", alias)

# Input del usuario
"""
first_name = input("Ingrese su nombre: ")
age = input("Ingrese su edad: ")

print("Hola ", first_name, ". Tu edad es: ", age) # Las variables name y age pueden cambiar dependiendo de lo que el usuario ingrese.
"""

# Cambiamos su tipo
name = 35
age = "John"
print(name)
print(age)

# Forzamos el tipo?
address: str = "Mi direccion"
address = True
address = 25
address = 2.5
print(type(address)) # Esto no genera error, pero no es buena practica cambiar el tipo de una variable.