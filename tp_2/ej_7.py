# Una persona invierte su capital en un banco y desea saber cuánto dinero ganará en un mes, teniendo en cuenta que el banco paga 2% mensual. ¿Cuánto ganará en seis meses si deja su dinero invertido?

INTERES_MENSUAL = 0.02
capital_invertido = int(input('Ingrese su capital invertido: '))

interes_ganado = capital_invertido * INTERES_MENSUAL

print('Su interes ganado en un mes es: $', interes_ganado)
