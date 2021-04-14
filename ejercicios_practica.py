#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

condicion = True   


def ej1():
    # Ejercicios con bucles "while"
    print("  Rta ej.1A  ")
    
    x = 0
    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea menor a 6>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" incremente "1" en cada iteración
    
    while x < 6:    # reemplace "condicion" por lo que crea necesario
            print("Valor de x =", x)
    # Coloque la línea de código para que "X" incremente "1"
            x +=  1
            print("Contador es =", x)
                                  
                        
    x = 5
    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea mayor o igual a 0>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" decremente "1" en cada iteración
    print("  Rta ej.1B  ")

    while x >= 0 :    # reemplace "condicion" por lo que crea necesario
        print("Valor de x =", x)
        # Coloque la línea de código para que "X" decremente "1"
        x = x - 1
        print ("Contador es =", x)

def ej2():
    # Ejemplos con bucles "for"
    print("  Rta ej.2  ")

    # Dado la siguiente lista de colores, utilizar "for"
    # para imprimir en pantalla todos los colores
    colores = ['rojo', 'naranja', 'verde', 'azul']
    
    for color in colores:
        print(color)
    
    # Itere el "for" utilizando la lista como parámetro
    # y utilizar como elemento del "for" cada color

    ######  no entiendo que hay que  hacer aca?   ######
    
            

    # Itere el "for" utilizando el tamaño de la lista
    # como parámetro y utilizar el índice para acceder a
    # los elementos de la lista
    
    colores_len = len(colores)
    colores_rango = range(colores_len)
    print("el rango es =", colores_rango)
    
    for i in colores_rango:
        if (i % 2) == 0:               # posiciones pares
            color_par = colores[i]
            print("en la posicion", i, "el color es =", color_par)
        else:
            color_impar = colores[i]   # posiciones impares
            print("en la posicion", i, "el color es =", color_impar)


def ej3():
    # Ejemplos con bucles "for"
    print("  Rta ej.3  ")
    
    # Dado la siguiente lista de números, utilizar "for"
    # para recorrer toda la lista y realizar la sumatoria de todos los números
    # La sumatoria se deberá ir guardando en la variable "suma"
    numeros = [1, 5, -1, 6, 10, 2, -5]
    suma = 0   # Variable ya inicializada, la suma arranca en cero


    for numero in numeros:
        suma = suma + numero
        print("la suma es ", suma)

def ej4():
    # Ejercicios con bucles "while"
    print("  Rta ej.4 , bucle 1 ")
    
    x = 0
    
    # Realizar un bucle "while" cuya condición de continuidad
    # sea que <x sea menor a 10> y que <x sea distinto de 6>
    # Colocar ambas condiciones como condicion del "while" realizando
    # una condición compuesta (utilice el operador "and" o "or" según corresponda) 
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print
    
    
    while True:
        if (x < 10) and (x != 6):
            print("el valor de x antes de incrementar es", x)    # valor de x antes de incrementar
            x_incrementada = x + 2
            print("el valor x incrementado es", x_incrementada)
            x = x_incrementada
        else:
            print(" Salimos del Bucle ")
            print(" ==> la 4ta iteracion no la hace" )
            print(" ==> porque la 2da condicion NO SE CUMPLE" )
            break

    print("  Rta ej.4 , bucle 2 ")
    x = 0         # inicializo de nuevo
    iteracion = 0

    # Realice el mismo bucle "while" pero en vez de estar formado por una condición
    # compuesta, que el "while" siga iterando mientras <x sea menor a 10>, y dentro del
    # "while" consultar si <x es igual a 6>, y en ese caso realizar una interrupción del bucle
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print
    
    while (x < 10):
        print("el valor de x es", x)    # valor de x antes de incrementar
        
        if (x == 6):
            print(" Salimos del Bucle ")
            print(" ==> porque SE CUMPLE LA CONDICION, x = ", x)
            break
            
        
        iteracion += 1
        print(" para la iteracion =", iteracion, "el valor de x es ", x)
        x_incrementada = x + 2         # valor de x luego de incrementar
        print("el valor x incrementado es", x_incrementada)
        x = x_incrementada    

def ej5():
    # Ejercicio de secuencias numéricas
    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y calcule a sumatoria total de todos los números dentro de esa secuencia
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior
    print("  Rta ej.5  ")
    
    secuencia_numerica = range(0,21,2)  # crea una lista de 10 elementos (hasta el 20)
    secuencia_len = len(secuencia_numerica)  # 11 posiciones va a tener
    print("Cantidad de posiciones de la secuencia numerica = ", secuencia_len)

    #inicio = int(input('Ingrese el primer número de la secuencia\n'))
    #fin = int(input('Ingrese el ultimo número de la secuencia\n'))
    

    sumatoria = 0
    for numero in secuencia_numerica:
        sumatoria += numero
        print("Para Numero =", numero, "Sumatoria es = ", sumatoria)



def ej6():
    # Ejercicio de secuencias numéricas
    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y cuante cuantos números son negativos y cuantos números son mayor o igual a cero
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior
    print("  Rta ej.6  ")
    
    #inicio = int(input('Ingrese el primero número de la secuencia\n'))
    #fin = int(input('Ingrese el ultimo número de la secuencia\n'))

    secuencia_numerica = range(-10,5,1)  # crea una lista de 15 elementos (hasta el 4)
    print(secuencia_numerica)

    secuencia_len = len(secuencia_numerica)
    print("Cantidad de posiciones de la secuencia = ", secuencia_len)
    
    cantidad_numeros_positivos = 0         # Inicializo el contador en 0
    cantidad_numeros_negativos = 0         # Inicializo el contador en 0
    
    for numero in secuencia_numerica:
        if (numero < 0):
            cantidad_numeros_negativos += 1
            print("Cantidad de numeros negativos es =", cantidad_numeros_negativos)
        else:
            cantidad_numeros_positivos += 1
            print("Cantidad de numeros positivos es =", cantidad_numeros_positivos)

   

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
    ej6()
