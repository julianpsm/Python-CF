elementos = {}
#añadir elementos
elementos['nombre'] = "Justcoddev"
elementos[(1, 2, 3)] = "La llave es una tupla"
#si no existe la llave la crea de lo contrario, se actualiza(el valor)
elementos['nombre'] = "Teddy Summers"
print(elementos)
print(len(elementos))

elementos = {'a': 1, 'b':2, 'c':3, 'a':4}
print(elementos)
print(len(elementos))