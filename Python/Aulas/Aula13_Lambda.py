# Syntax
# lambda arguments : expression

# mult args
x = lambda a, b, c=10: a + b + c
print(x(5, 8))

name = lambda nome: print(f"Olá, {nome}")
name("Garganel")


def dobro(n):
    return lambda a: a * n


myDo = dobro(2)  # value of n
print(myDo(10))  # value of a

triplicar = dobro(3)
print(triplicar(10))
