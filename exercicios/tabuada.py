#!/usr/bin/env python3

'''Praticando com f strings e format:
Programa que irá imprimir de maneira formatada e centralizada a tabuada do 1 ao 10.
'''

fatores = list(range(1,11))

for primeiro_fator in fatores:
    descricao = f' TABUADA DO {primeiro_fator} '
    print('\n' + '*' * 50)
    print('{:*^50}'.format(descricao))
    print('*' * 50 + '\n')
    for segundo_fator in fatores:
        produto = primeiro_fator * segundo_fator
        operacao = f'{primeiro_fator} x {segundo_fator} = {produto}'
        print('{:^50}'.format(operacao))

print('\n{:*^50}'.format(' FIM '))
