lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
#cambio
# [start:end]
# [start:]- > Obtenemos los últimos elementos de la lista
# [:end]-> Obtenemos los primeros elementos de la lista
# [start:end:skip]
sub_lista = lista_cursos[0:3]
sub_lista = sub_lista[1:5:2]
print(sub_lista)

