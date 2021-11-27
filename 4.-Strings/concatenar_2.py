nombre = 'Teddy'
apellido = 'Summers'

nombre_completo = nombre+" "+apellido
print(nombre_completo)

#usando %s
nombre_completo = 'Mr. %s %s %s.' %(nombre, apellido, "justcoddev")
print(nombre_completo)

#p
nombre_completo = 'Mr. {} {} {}.'.format(nombre,apellido, "justcoddev")
print(nombre_completo)

#w
nombre_completo = 'Mr. {_nombre} {_apellido} {marca}.'.format(
  _nombre= nombre,
  _apellido = apellido,
  marca=  "justcoddev"
)
print(nombre_completo)