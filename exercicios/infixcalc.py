#!/usr/bin/env python3

'''
Calculadora infix

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
infixcalc.py sum 5 2
7

infixcalc.py mul 10 5
50

infixcalc.py
operação: sum
n1: 5
n2: 4
9
'''

__version__ = '0.1.0'

import sys

arguments = sys.argv[1:]

if not arguments:
    operation = input('Operação: ')
    n1 = input('n1: ')
    n2 = input('n2: ')
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print('Invalid argument numbers.')
    print('ex: `div 40 5`')
    sys.exit(1)

operation, *nums = arguments

validated_nums = []
for num in nums:
    try:
        validated_nums.append(int(num))
    except ValueError:
        try:
            validated_nums.append(float(num))
        except ValueError:
            print(f'Invalid number: ${num}')

n1 = validated_nums[0]
n2 = validated_nums[1]

result = {
    'sum': n1 + n2,
    'sub': n1 - n2,
    'mul': n1 * n2,
    'div': n1 / n2
}
print(f'{result[operation]}')
