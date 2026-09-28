### Strings ###

my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string)) # Longitud de la variable
print(len(my_other_string)) # Longitud de la variable

print(my_string + " " + my_other_string) # Concatenación de strings
print(my_string, my_other_string) # Concatenación de strings con coma (agrega un espacio entre los strings)
print(my_string * 3) # Repetición de strings

my_new_line_string = "Este es un string\ncon un salto de línea"
print(my_new_line_string) # Salto de línea

my_tab_string = "Este es un string\tcon un tabulador"
print(my_tab_string) # Tabulador

my_scape_string = "\tEste es un string \n escapado" 
print(my_scape_string) # Escapando caracteres especiales

# Formateo de strings

name, surname, age  = "John", "Doe", 30

print("Mi nombre es {} {} y tengo {} años".format(name, surname, age)) # Formateo de strings con format()
print("Mi nombre es %s %s y tengo %d años" % (name, surname, age)) # Formateo de strings con %s y %d
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) # Formateo de strings con concatenación (se debe convertir el int a str forzando el tipo de dato)
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # Formateo de strings con f-strings (Python 3.6+)

# Desempaquetado de caracteres

language = "Python"
a, b, c, d, e, f = language
print(a) # Print desempaquetado de caracteres
print(b) # Print desempaquetado de caracteres
print(c) # Print desempaquetado de caracteres
print(d) # Print desempaquetado de caracteres
print(e) # Print desempaquetado de caracteres
print(f) # Print desempaquetado de caracteres


# División de strings

language_slice = language[1:3] # Slice de string (desde el índice 1 hasta el índice 3, sin incluir el índice 3)
print(language_slice) # Print slice de string

language_slice = language[1:] # Slice de string (desde el índice 1 hasta el índice 3, sin incluir el índice 3)
print(language_slice) # Print slice de string

language_slice = language[-2] # Slice de string (desde el índice 1 hasta el índice 3, sin incluir el índice 3)
print(language_slice) # Print slice de string

language_slice = language[1:2:4] # Slice de string (desde el índice 1 hasta el índice 3, sin incluir el índice 3)
print(language_slice) # Print slice de string

# Reverse

reversed_language = language[::-1]
print(reversed_language) # Print reverse de string

# Funciones 

print(language.capitalize()) # Capitaliza la primera letra del string
print(language.upper()) # Convierte el string a mayúsculas
print(language.lower()) # Convierte el string a minúsculas
print(language.count("t")) # Cuenta cuantas veces aparece un caracter en el string
print(language.isnumeric()) # Comprueba si el string es numérico
print("123".isnumeric()) # Comprueba si el string es numérico
print(language.startswith("Py")) # Comprueba si el string empieza con un caracter o string
print(language.endswith("on")) # Comprueba si el string termina con un caracter o string
print(language.upper().isupper()) # Comprueba si el string está en mayúsculas
print(language.startswith("Py").upper()) # Comprueba si el string empieza con un caracter o string y lo convierte a mayúsculas