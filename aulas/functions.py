numeros = [10, 12, 14, 20, 26, 30]
amigos = ['Marcos', 'Pedo', 'Adiana', 'Kalina', 'Marga']



amigos.sort()
print(amigos)

amigos.insert(2, 'Joao')
amigos.remove('Marga')
amigos.extend(numeros)
amigos.pop(1)
print(amigos)