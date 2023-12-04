import re

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

def valida(cnpj):
    cnpj = apenas_numeros(cnpj)

    try:
        if e_sequencia(cnpj):
            return False
    except Exception as e:
        return False

    try:
        novo_cnpj = calcula_digito(cnpj=cnpj, digito=1)
        novo_cnpj = calcula_digito(cnpj=novo_cnpj, digito=2)
    except Exception as e:
        return False

    return novo_cnpj == cnpj

def calcula_digito(cnpj, digito):
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regressivos = REGRESSIVOS
        novo_cnpj = cnpj
    else:
        return None

    total = sum(int(c) * r for c, r in zip(novo_cnpj, regressivos))
    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0

    return f'{novo_cnpj}{digito}'

def e_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    return sequencia == cnpj

def apenas_numeros(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)