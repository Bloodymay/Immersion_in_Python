#  Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
#  Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
#  Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

list_of_things = {'вода': 2, 'посуда': 2, 'спальник' : 2, 'одежда': 3, 'еда': 1,'снаряжение': 4}
load_capacity = int(input('Введите грузоподъемность рюкзака: '))
current_load = 0
current_filling_backpack = []
for el in list_of_things.items():

    if current_load <= load_capacity:
        if (load_capacity-current_load) < el[1]:
            continue
        else:
            current_filling_backpack.append(el[0])
            current_load += el[1]



print(f'Рюкзак заполнен на {current_load} кг. Вещи в нем: {str(current_filling_backpack) [1:-1]}')

