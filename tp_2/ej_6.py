# Ingresar tres números enteros, calcular su promedio y mostrarlo por pantalla.

TOTAL_NUMEROS = 3
primer_numero = int(input('Ingrese  primer numero: '))
segundo_numero = int(input('Ingrese segundo numero: '))
tercer_numero = int(input('Ingrese tercer numero: '))

promedio = (primer_numero + segundo_numero + tercer_numero) / TOTAL_NUMEROS
print('El promedio es : ', promedio)
