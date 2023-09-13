# Нарисовать в консоли ёлку спросив у пользователя количество рядов.
# rows = int(input('Введите количество строк: '))
# SYMBOL = '*'
# SPACE = ' '
# symbol_count = 1
# space_count = rows-1
# for row in range (rows):
#     print(SPACE * SPACE_COUNT + SYMBOL * SYMBOL_COUNT)
#     symbol_count += 2
#     space_count -= 1

rows = int(input('Введите количество строк: '))
SYMBOL = '*'
SPACE = ' '
symbol_count = 1
space_count = rows-1
STEP = 2
for row in range (rows):
    print(SPACE * (space_count - row) + SYMBOL * (symbol_count + row * STEP))
    # symbol_count += 2
    # space_count -= 1
