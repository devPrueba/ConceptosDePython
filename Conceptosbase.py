#exponenciacion
print(9**(1/2))
#Diviccion entera --> solo te retorna el valor entero y no muestra el decimal
print(20//6)
#modulo --> se utiliza para obtener el resto de una division
print(20 % 6)
print(1.25 % 0.5)
#cadenas de texto
print('Siempre mira el lado positivo de la vida')
#salto de linea
print("one\ntwo\ntree")
#operaciones con cadenas
print("spam"*3)
print(4*'2')
#variables -->Permite almacenar un valor asignandole un nom bre
user = "James"
#trabajando con variables
x1 = 123.456
x2 = "esto es un chanchito feliz"

print(x1)
print(x2)

x3=7
print("Esto es una potencia de 3 -->",x3**3)
#Entrada y salida sencilla
x = input("Ingrese un numero: ")
print(x)
nombre = input("Cual es tu nombre: ")
print(nombre)
#trabajar con entrada
edad = int(input("Ingrese su edad: "))
nombre = input("ingrese su nombre: ")
print("De "+nombre + " su edad es " + str(edad))
# operadores in situ
"""permiten escribir codigo como x = x + 2 de manera consisa
   como x += 3 que es lo mismo que x = x + 3
   lo mismo es posible utilizando otros signos *,-,/ y % """
x = 2
print(x)
x += 3 # se le sumo 3 a la variable x
print(x)
x = "a"
x*=3 # multiplica la variable x = "a" por 3
print(x)

# operador Walrus
"""permite asignar valores a las variables dentro de una
   expresion, incluidas las variables que aun no existen
   """
num = int(input()) # esto es una manera de hacerlo de manera normal
print(num)
print(num1:=int(input())) # esto es con el operador walrus que realiazas todas las operaciones a la vez

