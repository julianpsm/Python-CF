lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
lista_cursos_2 = ['C', 'C++', 'Docker']

print(len(lista_cursos))
lista_cursos.append('MongoDB')
lista_cursos.append('C#')
lista_cursos.append('Javascript')

lista_cursos.insert(1, 'Rails')
lista_cursos.insert(0, 'PyGame')
lista_cursos.extend(lista_cursos_2)

print(lista_cursos)

lista_cursos.remove('MongoDB')
del lista_cursos[0]

lista_cursos.clear()

print(len(lista_cursos))