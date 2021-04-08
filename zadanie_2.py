#!usr/bin/env python3
# - * - coding: utf - 8 -*-
#Определить, есть ли среди трёх заданных чисел нечётные.

import sys


if __name__ == '__main__':
    a = int(input('a-любое натуральное число ='))
    b = int(input('b- любое натуральное число ='))
    c = int(input('c- лбое натуральное число ='))
    if a % 2 == 0:
        print('Четное число')
    else:
        print('Нечетное число')
    if b % 2 == 0:
        print('Четное число')
    else:
        print('Нечетное число')
    if c % 2 == 0:
        print('Четное число')
    else:
        print('Нечетное число')
        exit(1)