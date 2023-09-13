user_number = int(input('Введите число в диапазоне 1 - 100000: '))
count = 0
MIN_VALUE = 1
MAX_VALUE = 100001
if MIN_VALUE < user_number < MAX_VALUE:
    for i in range(2, user_number // 2 + 1):
        if user_number % i == 0:
            count += 1

    if count == 0:
        print('Число простое')
    else:
        print('Число составное')
else:
    print('Неверное число! Введите число в диапазоне 1 - 100000')