# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
from fractions import Fraction
from math import gcd


str_1st = input('Введите первую дробь: ').split('/')
str_2nd = input('Введите вторую дробь: ').split('/')
str_1st_int = list(map(int,str_1st))
str_2nd_int = list(map(int,str_2nd))
if str_1st_int[1] == str_2nd_int[1]:
     print(f'Результат сложения дробей: {str_1st_int[0] + str_2nd_int[0]}/{str_1st_int[1]}')
else:
    common_denominator = int(str_1st_int[1] * str_2nd_int[1] / gcd(str_1st_int[1], str_2nd_int[1]))

    print(common_denominator)
print(f'Результат умножения дробей: {str_1st_int[0] * str_2nd_int[0]}/{str_1st_int[1] * str_2nd_int[1]}')
str_1st = '/'.join(str_1st)
str_2nd = '/'.join(str_2nd)
print(f'Результат умножения дробей через Fraction: {Fraction(str_1st) * Fraction(str_2nd)} ')
print(f'Результат сложения дробей через Fraction: {Fraction(str_1st) + Fraction(str_2nd)} ')