""" Una editorial determina el precio de un libro según la cantidad de páginas que
contiene. El costo básico del libro es de $500, más $3,20 por página con encua-
dernación rústica. Si el número de páginas supera las 300 la encuadernación
debe ser en tela, lo que incrementa el costo en $200. Además, si el número de
páginas sobrepasa las 600 se hace necesario un procedimiento especial de en-
cuadernación que incrementa el costo en otros $336. Desarrollar un programa
que calcule el costo de un libro dado el número de páginas. """


COSTO_BASICO = 500
ADICIONAL_PAGE_ENC = 3.20
COSTO_ADICIONAL_POR_TELA = 200
COSTO_ADICIONAL_ESPECIAL = 336
TOPE_BASICO = 300
TOPE_MAX_ESPECIAL = 600


total_pages = int(input('Ingrese las pagimas totales del libro: '))

if(total_pages <= TOPE_BASICO):
    costo_total = (total_pages * ADICIONAL_PAGE_ENC) + COSTO_BASICO
elif(total_pages > TOPE_BASICO and total_pages > TOPE_MAX_ESPECIAL):
    costo_total = (total_pages * ADICIONAL_PAGE_ENC) + (COSTO_BASICO + COSTO_ADICIONAL_POR_TELA)
else:
    costo_total = (total_pages * ADICIONAL_PAGE_ENC) + (COSTO_BASICO + COSTO_ADICIONAL_POR_TELA + COSTO_ADICIONAL_ESPECIAL)

print('El costo total del trabajo es de : $', costo_total)
