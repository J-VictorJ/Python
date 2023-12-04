# ### Python Variables
# 1. Declare uma variável chamada `nome` e atribua seu nome a ela. Em seguida, imprima a variável.
nome = "Chat GPT"
print(nome)

# 2. Declare três variáveis diferentes (`a`, `b` e `c`) e atribua valores inteiros a elas. Em seguida, some esses
# valores e armazene o resultado em uma quarta variável chamada `soma`. Imprima o valor de `soma`.
a, b, c = 2, 5, 8
soma = a + b + c
print(soma)
# 3. Declare uma variável chamada `frase` e atribua a ela uma string. Imprima a variável.
frase = "Valor de string"
print(frase)

# ### Python Data Types
# 4. Declare uma variável chamada `numero` e atribua a ela um número inteiro. Em seguida, converta essa variável para
# um número de ponto flutuante e imprima o resultado.
numero = 50
booleano = float(numero)
print(booleano)

# 5. Declare uma variável chamada `texto` e atribua a ela uma string que represente um número. Converta essa string para
# um número inteiro e imprima o resultado.

texto = "100"
inteiro = int(texto)
print(type(inteiro))

# ### Python Strings
#
# 6. Declare uma variável chamada `frase` com uma frase de sua escolha. Imprima o comprimento da string.
frase = "Roses are pink, violets are blue, and something happens no meu bucho"
print(len(frase))
# 7. Declare uma variável chamada `palavra` e atribua a ela uma palavra. Use o fatiamento de strings para imprimir a primeira letra da palavra.
palavra = "palavra"
print(palavra[0])
# 8. Declare uma variável chamada `frase1` com o valor "Olá" e outra variável chamada `frase2` com o valor "mundo".
# Combine essas duas variáveis para formar a frase "Olá mundo" e imprima o resultado.
frase1, frase2 = "Olá ", "mundo"
print(f"{frase1} {frase2}")
# 9. Declare uma variável chamada `nome` e atribua o seu nome a ela. Use a formatação de strings para criar uma
# mensagem personalizada que inclua o seu nome e imprima-a.
print(f"{nome}, Obrigado pela ajuda!")
# ### Python Booleans e Operators
#
# 10. Declare duas variáveis booleanas, `verdadeiro` e `falso`. Use operadores lógicos para criar uma expressão que seja
# verdadeira e outra que seja falsa. Imprima o resultado dessas expressões.
t = True
f = False
print(True) if t==True else print(False)
print(True) if f != 0 else print(False)
# 11. Declare uma variável chamada `idade` e atribua a ela a sua idade. Crie uma expressão que verifique se você é
# maior de 18 anos e imprima o resultado.
idade = 20
print("Maior de idade") if idade >= 18 else print("Menor de idade")

