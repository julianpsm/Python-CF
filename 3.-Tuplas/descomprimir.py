
uno, dos, tres, cuatro =1 ,2, 3, 4

print(uno)
print(dos)
print(tres)
print(cuatro)

#ahora con tuplas
numeros = (1, 2, 3, 4, 5, 6)
uno, dos, tres, cuatro, * resto_valores = numeros
#cuando no son asignados a variables se los muestra así, se da cuenta python
#creando nueva lista colocando el * como prefijo, ya que son valores que n ose desenpaquetan
# y si no deseamos trabajar con esos valores simplemente se coloca lo siguiente
# asterisco guion bajo = *_
print(uno)
print(dos)
print(tres)
print(cuatro)
print(resto_valores)


