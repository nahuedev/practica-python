#Una inmobiliaria paga a sus vendedores un salario de $50000, más una comisión de $5000 por cada venta realizada, más el 5% del valor de las ventas.
#Realizar un programa que imprima el número del vendedor y el salario que le corresponde en un determinado mes.
#Se leen el número del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.

salario = 50000
comision_fija = 5000
tasa_comision_variable = 1.05

numero_vendedor = input('Ingrese el numero de vendedor: ')
ventas_del_mes = int(input('Ingrese las ventas del mes: '))
valor_ventas_mes = int(input('Ingrese el valor total de la ventas del mes: '))

comision_por_venta = ventas_del_mes * comision_fija
comision_variable = comision_por_venta * tasa_comision_variable

print('Salario del mes: $', salario)
print('Comision por ventas del mes: $', comision_por_venta)
print('Comision variable por ventas del mes: $', comision_variable)
