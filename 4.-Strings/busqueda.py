titulo_curso = 'Curso profesional de Python - Python'

#método count -> recibe como argumento un string
#en este caso un string que nosotros queremos conocer si existe o no
#dentro del string base

contador = titulo_curso.count('Python')
print(contador)

#mediante boolean
#con la palabra reservada "in" y usando
# método lower, convierte todo en minuscuca y lo busca
print('python' in titulo_curso.lower())
print('python4000' not in titulo_curso.lower())

#conocer si un string se encuentra al inicio del string
print(titulo_curso.startswith('Curso'))
#conocer si un string se encuentra al final del string
print(titulo_curso.endswith('Python'))