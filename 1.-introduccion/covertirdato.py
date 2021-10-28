nombre_completo = input('Ingresa tu nombre completo: ')
print(nombre_completo)
print(type(nombre_completo))

edad = int(input('Ingresa tu edad: '))
print(edad)
print(type(edad))

altura = float(input('Ingresa tu altura: '))
print(altura)
print(type(altura))

autoriacion = input('¿Autorizas el programa? (si/no) ')
# autoriacion = input('¿Autorizas el programa? (si/no) ') == 'si'  ----> mas eficiente
autoriacion = autoriacion == 'si'
print(autoriacion)
print(type(autoriacion))