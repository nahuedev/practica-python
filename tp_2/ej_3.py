# Calcular el promedio de las notas que obtiene un alumno al rendir los dos parciales

CANT_PARCIALES = 2
nota_primer_parcial = int(input('Ingrese nota primer parcial: '))
nota_segundo_parcial = int(input('Ingrese nota segundo parcial: '))

promedio = (nota_primer_parcial + nota_segundo_parcial)/CANT_PARCIALES
print('El promedio es : ', promedio)
