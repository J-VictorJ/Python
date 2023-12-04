"""nome = 'João'
idade = 19
altura = 1.92
peso = 120
imc = peso / (altura * altura)
nascimento = 2022 - idade - 1

print(f'{nome} tem {idade} anos, {altura} de altura, e pesa {peso} KG')
print(f'O seu imc é {imc:.3f}')
print(f'o ano de nascimento é {nascimento}')

#Ever, EVER, use f str with {} EVER
    """


"""x = int(input('Digite o primeiro '))

b = x % 4 == 0
if b is True:
    print('Ano bissexto')
elif b is not True:
    print('Não é bissexto')
"""


"""nome = input('Digite seu nome ')
tam = len(nome)

if tam <= 4:
    print('vosso nome curto és!')
elif tam <= 5 and tam <= 6:
    print('Nome normal!')
elif tam >= 7:
    print('Nome muito grande!')
else:
    print('digite seu nome!!!')"""


"""
# Numeros de forma progressiva e regressiva
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
for y, x in enumerate(range(10, 1, -1)):
    print(x, y)

"""


"""# Validador de CPF
from random import randint
numero = str(randint(100000000, 999999999))

novo_cpf = numero                   # 9 números aleatórios
reverso = 10                        # Contador reverso
total = 0                           # O total das multiplicações

# Loop do CPF
for index in range(19):
    if index > 8:                   # Primeiro índice vai de 0 a 9,
        index -= 9                  # São os 9 primeiros digitos do CPF

    total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

    reverso -= 1                    # Decrementa o contador reverso
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:                   # Se o digito for > que 9 o valor é 0
            d = 0
        total = 0                   # Zera o total
        novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

print(novo_cpf)
"""


"""'''1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
'''

def saudacao(saudacao, nome):
    print(f'{saudacao} {nome}')

saudacao('Olá', 'Joãozinho')
saudacao('Oi', 'Maria')
saudacao('Hey', 'Eduardo')



'''2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre 
eles.
'''

def soma(n1, n2, n3):
    print(n1 + n2 + n3)


soma(2, 1, 3)
soma(1, 1, 1)
soma(2, 1, 1)


'''3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
'''

def aumento_percentual(valor, percentual):
    return valor + (valor * percentual / 100)


ap = aumento_percentual(50, 10)
print(ap)
ap = aumento_percentual(100, 10)
print(ap)
ap = aumento_percentual(10, 10)
print(ap)
ap = aumento_percentual(15, 100)
print(ap)


'''
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
'''


def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizzbuzz, {n} é divisível por 3 e 5'
    if n % 5 == 0:
        return f'buzz, {n} é divisível por 5'
    if n % 3 == 0:
        return f'fizz, {n} é divisível por 3'
    return n


from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))
"""


"""x = int(input('Qual tabuada queres ver '))

while True:
    for numero in range(1, 11):
        n = x * numero
        print(f'{x} x {numero} = {n}')
"""


"""perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3x2? ',
        'respostas': {
            'a': '4',
            'b': '101',
            'c': '6',
        },
        'resposta_certa': 'c',
    },
}
print()
respostas_certas = 0
for pergunta, dados_pergunta in perguntas.items():
    print(f'{pergunta}: {dados_pergunta["pergunta"]}')

    print('Respostas: ')
    for resposta, dados_resposta in dados_pergunta['respostas'].items():
        print(f'[{resposta}]: {dados_resposta}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == dados_pergunta['resposta_certa']:
        print('Você acertou!!!!')
        respostas_certas += 1
    else:
        print('Você ERROU!!!!')

    print()

quantidade_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / quantidade_perguntas * 100
print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%.')"""


"""'''
-> É uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados
Exercício
-> Crie uma função que encontra o primeiro duplicado considerando o segundo
    número como a duplicação. Retorne a duplicação considerada.
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda
            ocorrência do número, ou seja, o número duplicado em si.
            Exemplo:
                [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
                [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
            Se não encontrar duplicados na lista, retorne -1
'''
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]
def cacaNum(lista_de_listas_de_inteiros):
    numerosChecados = set()
    primeiroDupl = -1
    for numero in lista_de_listas_de_inteiros:
        if numero in numerosChecados:
            primeiroDupl = numero
            break
        numerosChecados.add(numero)
    return primeiroDupl


for lista_de_listas_de_inteiros in lista_de_listas_de_inteiros:
    print(lista_de_listas_de_inteiros, cacaNum(lista_de_listas_de_inteiros))
    """


"""string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10
l1 = [string[i:i +n] for i in range(0, len(string), n)]
retorno = '.'.join(l1)
print(l1)
print(retorno)
"""


"""carrinho = []
carrinho.append(('produto 1', 30))
carrinho.append(('produto 2', 20))
carrinho.append(('produto 3', 50))

total = sum(int(y) for x, y in carrinho)
print(total)

# List compr... here use the y only, ok, but the great problem is, I can't sum all, and use the sum function have give
# me the solution, y cannot be int sometimes I convert he, and put all inside of sum
"""


"""pontos = 0

print("Responda apenas com sim ou não: ")

a = (input("Telefonou para a vítima? "))
if a == 'sim':
    pontos = pontos + 1
else:
    pontos = pontos + 0

b = (input("Esteve no local do crime?  "))
if b == 'sim':
    pontos = pontos + 1
else:
    pontos = pontos + 0

c = (input("Mora perto da vítima?  "))
if c == 'sim':
    pontos = pontos + 1
else:
    pontos = pontos + 0

d = (input("Devia para a vítima?  "))
if d == 'sim':
    pontos = pontos + 1
else:
    pontos = pontos + 0

e = (input("Já trabalhou com a vítima?  "))
if e == 'sim':
    pontos = pontos + 1
else:
    pontos = pontos + 0
    
print()

print(f"você fez {pontos} pontos")

if pontos == 2:
    print("Classificado como: Suspeito")
elif pontos == 3 or pontos == 4:
    print("Classificado como: Cúmplice")

elif pontos == 5:
    print("Classificado como: Assassino")

elif pontos == 0:
    print("Classificado como: Inocente")
    """


"""menor = 100000000
for x in range(3):
    y = int(input('Digite ')) #12 5 2
    if y < menor:
        menor = y
        print(f'só vou executar se for verdade, {menor}')
    print(f'maior² é, {menor}')

print(menor)
"""


"""
media = 0
soma = 0
for x in range(6):
    y = int(input('Digite '))
    soma += y
    media = (media + soma) / 6
print(soma)
print(f'{media:.1f}')
"""


"""for x in range(0, 51):
    if x % 2 != 0:
        print(x, end=', ')
"""


"""x = int(input("digite um numero--> "))
y = int(input("digite outro numero--> "))

for i in range(x, y + 1):
    print(i, end=', ')
    
print('=' * 30)
for i in range(x, y + 1):
    soma += i
    print(i, end=', ')
print()
print(f'A soma de {x} até {y} é: {soma}')

"""


"""numero = int(input("Fatorial de: "))

resultado = 1
count = 1

while count <= numero:
    resultado *= count
    count += 1
print(resultado)
"""


"""l1 = [2, 7, -8, 6, 5]
l2 = [8, 3, 18, 4, 5]

l3 = [x + y for x, y in zip(l1, l2)]
print(l3)
"""


"""'''
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa
'''


def show_op(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()


def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Nada a desfazer')
        return

    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a refazer')
        return

    last_redo = redo_list.pop()
    todo_list.append(last_redo)


def do_add(todo, todo_list):
    todo_list.append(todo)


if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Digite uma tarefa ou undo, redo, ls: ')

        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            do_undo(todo_list, redo_list)
            continue
        elif todo == 'redo':
            do_redo(todo_list, redo_list)
            continue

        do_add(todo, todo_list)"""


"""print('What verb do you want?')
verb = input('Press a verb ')

if 'o, s, x, sh, ch' in verb:
    print(f'add "ES" {verb}es'
          f'I {verb}'
          f'You {verb}'
          f'He {verb}es'
          f'She {verb}es'
          f'It {verb}es'
          f'We {verb}'
          f'You {verb}'
          f'They {verb}')

elif 'a, e, i, o, u, y' in verb:
    print(f'add "S" {verb}s')

elif 'a, e, i, o, u, y' not in verb:
    new = verb[:-1]
    print(f'add "IES" - Y, {new}ies')

elif 'have' in verb:
    print('add "HAS"')

else:
    print(f'S {verb}s')

"""