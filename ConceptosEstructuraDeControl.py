#Boleanos y comparaciones

"""
Otro tipo en python es el tipo booleano. hay dos valores booleanos
True , False
Se pueden crear comparando valores, por ejemplo utilizando el operador "==".
"""
mi_booleano = True
print(mi_booleano) # resultado True
print(2 == 3) # Resultado False
print("hola" == "hola") # Resutado True

"""Otro operador es el "!=" operador no es igual, Se evalua como True si los elementos que se comparan
   no son iguales y False si lo son."""

print(1 != 1) # False
print( "once" != "siete" ) # True
print(2 != 10) # True

"""Comparacion Menor que "<", Mayor que ">"  """

print(7 > 5) # True
print(10< 10 ) #False

"""Los operadores mayor o igual que y menor o igual que (>= y <=) son similares a los anteriores 
   ecepto que vuelven True al comparar numeros iguales (8>=8) o (7<=7)"""

print(7 <= 8) # True
print(9 >= 9.0) # True

# Declaraciones COndicionales "if"
"""Puedes utilizar if para ejecutar codigo si cumple una determinada condicion
   Si una expresion se evalua como True, se llevean acabo algunas declaraciones
   De lo contrario no se llevan a cabo"""

if 10 > 5:
    print("10 es mayor que 5") # se cumple la declaracion siempre que se cumpla la condicion
print("programa Finalizado")

"""Para realiazar comprobaciones mas complejas, si las sentencias se pueden anidar , una dentro de otra
   Esto significa que la instruccion "if" interna es parte de instrucciones de la externa.Esta es una
   forma de ver si cumple varias condiciones."""

num = 12 # la indentacion se utiliza para definir el nivel de anidacion
if num >5:
    print("Mayor que 5")
    if num <=47:
        print("Entre 5 y 47")

#Sentencia else
"""La declaracion (if) permite comprobar una una condicion y ejecutar algunas declaraciones, si la condion es True
   La declaracion (else) puede ser usada para ejecutar algunas declaraciones cuando la condicion de la declaracion
   "if" es Falsa """

x = 4
if x ==5: #tener en cuenta los ( : ) despues de la palabra clave (if o else)
    print("Si")
else:
    print("no")

num = 3
if num==1:
    print("uno")
else:
    if num==2:
        print("dos")
    else:
        if num==3:
            print("tres")
        else:
            print("Otra cosa")

#Declaracion elif
"""Multiples declaraciones ( if/else ) hacen que el codigo sea largo y poc legible 
   la declaracion elif (abreviatura de else if) es una atajo para usar cuando se encadenan declaraciones
   ( if y else), haciendo el codigo mas corto"""

num = 3
if num==1:
    print("uno")
elif num==2:
    print("dos")
elif num==3:
    print("tres")
else:
    print("Otra cosa")

#Logica Booleana

"""Se utiliza para crear condiciones mas complicadas para la declaracion if que se basan en mas de una condicion
   Los operadores booleanos de Python son : (and, or, not)
   El operador and toma dos argumentos y se evalua como True. De lo contrario,se evalua como false"""
# los operadores booleanos se pueden usar tantas veces como sea necesario
print(1 == 1 and 2 == 2) # True
print(1 == 1 and 2 == 3) # False
print(1 != 1 and 2 == 2) # False
print(2 < 1 and 3 > 6) # False
# or toma tambien dos argumentos y evalua si uno o los dos se cumplen caso contrario
# sera falso el resultado que se obtendra
print(1 == 1 or 2 == 2) #True
print(1 == 1 or 2 == 3) #True
print(1 != 1 or 2 == 2) #true
print(2 < 1 or 3 >  6) #False
# not toma un argumento y lo invierte y el Resultado de un No Verdadero es Falso y no Falso va a Verdadero
print(not 1 == 1) # False
print(not 1 > 7) # true
# ( == ) tiene una precedencia mas alta que ( or )
print(False == False or True) # True
print(False == (False or True)) # False
print((False == False) or True) # True