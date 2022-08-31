""" Ingresar las notas de los dos parciales de un alumno e indicar si promocionó,
aprobó o si debe recuperar. Informar un error si el valor de alguna nota no está
entre 0 y 10.
- Se promociona cuando las notas de ambos parciales son mayores o
iguales a 7.
- Se aprueba cuando las notas de ambos parciales son mayores o iguales
a 4.
- Se debe recuperar cuando al menos una de las dos notas es menor a 4. """


NOTA_MIN = 1
NOTA_MAX = 10

nota_primer_parcial = int(input('Ingrese la nota del primer parcial: '))


if(nota_primer_parcial < NOTA_MIN or nota_primer_parcial > NOTA_MAX ):
    print('La nota del primer parcial es incorrecta')
else:
    nota_segundo_parcial = int(input('Ingrese la nota del segundo parcial: '))
    if(nota_segundo_parcial < NOTA_MIN or nota_segundo_parcial > NOTA_MAX ):
        print('La nota del segundo parcial es incorrecta')
    elif(nota_primer_parcial >= 7 and nota_segundo_parcial >=7 ):
        print('Promocion')
    elif(nota_primer_parcial >= 4 and nota_segundo_parcial >= 4):
        print('Cursada aprobada')
    elif(nota_primer_parcial < 4 or nota_segundo_parcial < 4):
        print('Se debe recuperar almenos un examen')


