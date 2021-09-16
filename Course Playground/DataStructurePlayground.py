# Listas
lista = [6, 1, 22, 15]
print(lista)
lista.append(16)  # Añadir Item
print(lista)
lista.remove(15)  # Remover Item
print(lista)
lista.sort()  # Ordenar Items
print(lista)
print()

# Sets
setT = {1, 1, 22, 15}  # Los set se crean con {} no con []
setT.add(1)  # Los set no repiten items, son unicos
print(setT)
print()

# Diccionarios
d = {
    'Bob': 0,
    'Alex': 0,
    'derrotadoPor': {'Papel', 'Sample'},
    'derrotaA': {'Sponja', 'Tijeras'}
}

# Ctrl + / = Comentar Multiples Lineas
#d = dict(joe:'5', billie: '9', zoe: '6')
#name = 'zoe'
#print(f"Victorias de {name}: {d[name]}")
# wins = d.get(name)
# if wins:
#     print(f"Tiene {wins} victorias.")
# else:
#     print("No ha jugado.")

print(d['Bob'])
d['Bob'] += 1
print(d['Bob'])
print(d)
d['Sam'] = 6
print(d)
print(f"Eres derrotado por {d['derrotadoPor']}")
print(d.get('Otro', 61))  # Comprobar si un item esta en el diccionario, retorna 61 y no None
