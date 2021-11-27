lenguajes = '1 Python Ruby Java Rust C++ C'

#split() nos permite generar una lista a partir de un string
listado_lenguajes = lenguajes.split()
print(listado_lenguajes)

#split no puede dividir el string mediante -, debe detectar el ESPACIO
#la solución a esto, es
lenguajes_2 = '2-Python-Ruby-Java-Rust-C++-C'
#colocando dentro de los parentesis como argumento, el caracter o los caracteres
#a partir de los cuales queremos dividir el string, en este caso "-", siempre y cuando
#este existe en el string
listado_lenguajes_2 = lenguajes_2.split('-')
print(listado_lenguajes_2)

lenguajes_2 = '3//Python//Ruby//Java//Rust//C++//C'
listado_lenguajes_2 = lenguajes_2.split('//', 2) # total de espacios que separará el string

print(listado_lenguajes_2)

#.................................................
#lista a string
lenguajes_4 = ['4', 'Python', 'Ruby', 'Java', 'Rust', 'C++', 'C']

string_lenguajes = '-'.join(lenguajes_4)
print(string_lenguajes)
print(type(string_lenguajes))