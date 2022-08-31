""" Leer tres números correspondientes al día, mes y año de una fecha e imprimir
un mensaje indicando si la fecha es válida o no. """

dia = int( input('Ingrese el dia de la fecha: '))
mes = int(input('Ingrese el numero de mes de la fecha: '))
anio = int(input('Ingrese el año de la fecha '))

if((dia > 0  or dia <= 31)):
    print( (dia > 0 or dia <= 31))
    print('La fecha ingresada es correcta')
else:
    print('La fecha ingresa no es valida')
