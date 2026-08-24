### Operadores ### Operadores Aritméticos

print(3 + 4) # Suma
print(3 - 4) # Resta
print(3 * 4) # Multiplicación
print(3 / 4) # División
print(3 // 4) # División entera
print(10 % 2) # Módulo
print(3 ** 4) # Potencia
print(3 + 4 * 2) # Orden de operaciones (Primero multiplicación, luego suma)
print((3 + 4) * 2) # Orden de operaciones con paréntesis (Primero paréntesis, luego multiplicación)
print(3 + 4 * 2 ** 2) # Orden de operaciones con potencia (Primero potencia, luego multiplicación, luego suma)

print("Hola" + "Python" + "¿Qué tal?") # Concatenación de strings
print("Hola" + str(5)) # Concatenación de string con int (se debe convertir el int a str forzando el tipo de dato)
print("Hola" + str(5) + "¿Qué tal?") # Concatenación de string con int (se debe convertir el int a str forzando el tipo de dato)
print("Hola " * 5) # Repetición de strings
print("Hola " * (2 ** 3)) # Repetición de strings con potencia

my_float = 2.5 * 3
print("Hola " * int(my_float)) # Repetición de strings con float (se debe convertir el float a int forzando el tipo de dato)

### Operadores de Comparación ###

print(3 > 4) # Mayor que
print(3 < 4) # Menor que
print(3 >= 4) # Mayor o igual que
print(3 <= 4) # Menor o igual que 
print (3 == 4) # Igual que
print(3 != 4) # Diferente que

print("Hola" > "Python") # Comparación de strings (se compara el valor ASCII de cada caracter)
print("Hola" < "Python") # Comparación de strings (se compara el valor ASCII de cada caracter)
print("aaaa:" >= "abaa") # Comparación de strings (se compara el valor ASCII de cada caracter) 
print("Hola" <= "Python") # Comparación de strings (se compara el valor ASCII de cada caracter)
print ("Hola" == "Python") # Comparación de strings (se compara el valor ASCII de cada caracter)
print("Hola" != "Python") # Comparación de strings (se compara el valor ASCII de cada caracter)


#### Operadores Lógicos ###

print(True and True) # AND
print(3 > 4 and "Hola" > "Python") # AND
print(True or False) # OR
print(3 > 4 or "Hola" > "Python") # OR
print(not True) # NOT
