""" Ingresar dos números enteros e indicar si son iguales o distintos """


first_number= int(input('Ingrese un número'))
second_number= int(input('Ingrese un segundo numero'))

if (first_number == second_number):
    message = 'Son iguales'
else:
    message = 'Son distintos'

print(message)
