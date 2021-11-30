mensaje = 'Hola mundo!'
# ljust -> Justificar a la izquierda
# rjust -> Justificar a la derecha
# center -> Centrae

mensaje = mensaje.ljust(22)
print(mensaje, ".")

mensaje = mensaje.rjust(22)
print(mensaje, ".")

mensaje = mensaje.center(20)
print(mensaje)