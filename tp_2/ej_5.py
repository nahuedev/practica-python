# Tres personas invierten dinero para fundar una empresa (no necesaria-mente en partes iguales). Calcular qué porcentaje invirtió cada una

primera_inversion = int(input('Ingrese el  primer capital invertido: '))
segunda_inversion = int(input('Ingrese el  segundo capital invertido: '))
tercera_inversion = int(input('Ingrese el  tercer capital invertido: '))

total_invertido = primera_inversion + segunda_inversion + tercera_inversion

print('Total invertido: ', total_invertido)

porcentaje_primera_inversion = (primera_inversion * 100) / total_invertido
porcentaje_segunda_inversion = (segunda_inversion * 100) / total_invertido
porcentaje_tercera_inversion = (tercera_inversion * 100) / total_invertido

print('Capital invertido: ', porcentaje_primera_inversion, '%')
print('Capital invertido: ', porcentaje_segunda_inversion, '%')
print('Capital invertido: ', porcentaje_tercera_inversion, '%')
