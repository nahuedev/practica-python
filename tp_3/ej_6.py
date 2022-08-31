""" Una remisería requiere un programa que calcule el precio de un viaje a partir de
la cantidad de kilómetros que desea recorrer el usuario. Para eso cuenta con la
siguiente tarifa:
- Viaje mínimo $250. Sólo se cobra cuando el importe por kilómetro no
alcanza este mínimo.
- Si recorre entre 0 y 10 km: $30 por km
- Si recorre 10 km o más: $20 por km """


VIAJE_MINIMO = 250
TOPE_PRIMERA_SECCION = 10
PRECIO_PRIMERA_SECCION  =30
PRECIO_MAX = 20

kilometros_viaje = int(input('Ingrese la cantidad de kilometros del viaje: '))

if(kilometros_viaje >= 0 and kilometros_viaje < TOPE_PRIMERA_SECCION):
    costo_viaje = kilometros_viaje * PRECIO_PRIMERA_SECCION
else:
    costo_viaje = kilometros_viaje * PRECIO_MAX

if(costo_viaje < VIAJE_MINIMO):
    costo_viaje = VIAJE_MINIMO

print('El costo del viaje es de : $', costo_viaje)