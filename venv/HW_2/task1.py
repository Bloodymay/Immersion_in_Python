# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
user_num = int(input('Введите целое число: '))
user_num_check = user_num
HEXADECIMAL_SYMBOLS = '0123456789ABCDEF'
hexadecimal_number = []

while user_num > 0:
    symbol = user_num % 16
    hexadecimal_digit = HEXADECIMAL_SYMBOLS[symbol]
    hexadecimal_number.insert(0, hexadecimal_digit)
    user_num //= 16

print(f'Шестнадцатеричное число: 0x{"".join(map(str, hexadecimal_number))}')
print(f'Шестнадцатеричное число через функцию "HEX": {hex(user_num_check)}')