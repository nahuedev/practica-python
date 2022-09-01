""" Leer un número correspondiente a un año e imprimir un mensaje indicando si es
bisiesto o no. Un año es bisiesto cuando es divisible por 4. Sin embargo, aquellos
años que sean divisibles por 4 y también por 100 no son bisiestos, a menos que
también sean divisibles por 400. Por ejemplo, 1900 no fue bisiesto pero sí el
2000. """

anio  = int(input('Ingese un año para saber su caracteristica: '))

""" if((anio % 4 != 0 and anio % 100 != 0) or anio % 400 != 0  ):
    print('El año ingresado no es bisiesto')
else:
    print('El año ingresado  es bisiesto')
     """



if(not anio % 4 and (anio % 100 or not anio % 400)):
        print('bisiesto')
else:
    print('El año ingresado no es bisiesto')
