lista = [1, 2, 3, 4, 5]
#si hay elementos demás estos simplementes son omitidos,
#deben tener la misma longitud

tupla = (10, 20, 30, 40, 50)

lista_2 =[100, 200, 300, 400, 500]

tupla_2 = (1000, 2000, 3000, 4000, 5000)

resultado = zip(lista, tupla, lista_2, tupla_2) # -> zip
#lo mas recomendabler  es usar tuple con zip
resultado = tuple(resultado)
resultado = list(resultado)

print(resultado)