# Python Lists
# Crie uma lista chamada frutas com três nomes de frutas de sua escolha. Em seguida, imprima a lista.
frutas = ["Banana", "Uva", "Maça"]
print(frutas)

# Acesse o segundo item da lista frutas e o último item da lista usando índices. Imprima esses itens separadamente.
print(frutas[1])
print(frutas[-1])

# Altere o terceiro item da lista frutas para outra fruta de sua escolha. Imprima a lista atualizada.
frutas[2] = "Limão"
print(frutas)

# Adicione uma nova fruta à lista frutas usando o método append(). Imprima a lista atualizada.
frutas.append("Pêra"), print(frutas)

# Remova a segunda fruta da lista frutas usando o método remove(). Imprima a lista após a remoção.
frutas.remove(frutas[1])
print(frutas)

# Crie uma lista chamada numeros com os números de 1 a 5. Use um loop for para percorrer a lista e imprimir cada número.
numeros = [1, 2, 3, 4, 5]
for n in numeros:
    print(n)
# Crie uma nova lista chamada quadrados que contenha o quadrado de cada número da lista numeros. Use list comprehension
# para criar essa lista.

quadrados = [x ** 2 for x in numeros]
print(quadrados)
# Ordene a lista numeros em ordem decrescente usando o método sort(). Em seguida, imprima a lista ordenada.
numeros.sort(reverse=True)
print(numeros)
# Crie uma cópia da lista frutas chamada frutas_copia. Modifique a frutas_copia para incluir uma fruta adicional e,
# em seguida, imprima tanto a lista original quanto a cópia.

frutas_copia = frutas.copy()
frutas_copia.append("Uva")
print(frutas), print(frutas_copia)

# Crie uma segunda lista chamada outras_frutas com três nomes de frutas diferentes. Use o método extend() para
# adicionar os elementos da lista outras_frutas à lista frutas. Imprima a lista resultante.

outras_frutas = ["pepino", "tomate", "beringela"]
frutas.extend(outras_frutas)
print(frutas)
