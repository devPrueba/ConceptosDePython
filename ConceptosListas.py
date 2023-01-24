# Listas
"""
    Las listas se utilizan para almacenar elementos.Se crea una lista utilizando
    corchetes con comas que separan los elementos.
"""
words = ["Hello", "world", "!"]
#   Se puede acceder a un determinado elemento de una lista utilizando su indice entre corchetes
print(words[0])  # En la posicion (0) Hello
print(words[1])  # En la posicion (1) world
print(words[2])  # En la posicion (2)   !

str = "Hello world!"
print(str[0])  # Accedes al indice de la cadena de caracteres como si fuera una lista

# Operaciones con listas
nums = [1, 2, 3]
print(not 4 in nums)  # True
print(4 not in nums)  # True
print(not 3 in nums)  # False
print(3 not in nums)  # False

#Funciones de listas

nums = [1, 2, 3]
nums.append(4) # append --> Agrega el numero 4 al final de la lista de [1, 2, 3 ] --> [1, 2, 3, 4]
print(nums)

nums = [1, 2, 3, 2, 4]
print((len(nums))) # obtiene el numero de elementos de una lista

words =["Puthon","fun"]
index = 1 # es la posicion que queremos a la que le asignamos una variable
words.insert(index,"is") # insert --> es similar a append salvo que permite insertar un nuevo elemento en cualquier posiion de las lista
print(words)

letters = ['p', 'q', 'r', 's', 'p', 'u','z']
print(letters.index('r')) # Index --> encuentra la primera aparicion de un elemento de la lista y devuelve su indice
print(letters.index('p')) # Si el elemento no esta en la lista muestra un elemento  ValueError
print(letters.index('z'))

letters1 = ['0', '1', '9', '2', '3', '5','9']
print("Encuentra el Maximo Valor que es: ",max(letters1))
print("Encuentra el Minimo Valor que es: ",min(letters1))
print("Cuenta las veces que apararece un elemento en la lista: ",letters1.count('9'))
print("Elimina un elemento en la lista: ",letters1.remove('0'))
print(letters1)
print("invierte los elemento en una lista: ",letters1.reverse())
print(letters1)
