#Una inmobiliaria paga a sus vendedores un salario de $50000, más una comisión de $5000 por cada venta realizada, más el 5% del valor de las ventas.
#Realizar un programa que imprima el número del vendedor y el salario que le corresponde en un determinado mes.
#Se leen el número del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.

SALARIO = 50000
COMISION_FIJA = 5000
TASA_COMISION_VARIABLE= 1.05

numero_vendedor = input('Ingrese el numero de vendedor: ')
ventas_del_mes = int(input('Ingrese las ventas del mes: '))
valor_ventas_mes = int(input('Ingrese el valor total de la ventas del mes: '))

comision_por_venta = ventas_del_mes * COMISION_FIJA
comision_variable = comision_por_venta * TASA_COMISION_VARIABLE

print('Salario del mes: $', SALARIO)
print('Comision por ventas del mes: $', comision_por_venta)
print('Comision variable por ventas del mes: $', comision_variable)
