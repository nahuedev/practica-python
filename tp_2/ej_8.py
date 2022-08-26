
#Leer una medida en metros e imprimir esta medida expresada en centí-metros, pulgadas, pies y yardas. Los factores de conversión son:

#1 pie = 12 pulgadas
#1 yarda = 3 pies
#1 pulgada = 2,54 cm.
#1 metro = 100 cm


CENTIMETROS = 100
PULGADA = 2.54
PIE = 12
YARDAS = 3 
medida_en_metros = int(input('Ingrese la medida en metros a convertir: '))

print('Su medida es equivalente a : ')
print('En centimetros:', medida_en_metros * CENTIMETROS, 'cm')

print('En pulgadas:', (medida_en_metros * CENTIMETROS) / PULGADA, 'pulgadas')
print('En pies:', ((medida_en_metros * CENTIMETROS) / PULGADA) / PIE, 'pies')
print('En yardas:', (((medida_en_metros * CENTIMETROS) / PULGADA) / PIE) / YARDAS , 'yardas')
