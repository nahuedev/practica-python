""" Desarrollar un programa que solicite un número de mes (por ejemplo 4) y
escriba el nombre del mes en letras ("abril"). Verificar que el mes sea válido y
mostrar un mensaje de error en caso de que no lo sea. """

TOPE_MIN= 1
TOPE_MES= 12

mes = int(input('Ingrese numero de mes'))


if(mes < TOPE_MIN or mes > TOPE_MES ):
    print('ERROR.Mes invaldio')
elif(mes == 1 ):
    print('Enero')
elif(mes==2):
    print('Febrero')
elif(mes==3):
    print('Marzo')
elif(mes==4):
    print('Abril')
elif(mes==5):
    print('Mayo')
elif(mes==6):
    print('Junio')
elif(mes==7):
    print('Julio')
elif(mes==8):
    print('Agosto')
elif(mes==9):
    print('Septiembre')
elif(mes==10):
    print('Octubre')
elif(mes==11):
    print('Noviembre')
elif(mes==12):
    print('Diciembre')