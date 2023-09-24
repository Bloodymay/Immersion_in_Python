# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

user_list = input('Введите массив данных через пробел:').split()
for el in set(user_list):
    if user_list.count(el) < 2:
        user_list.remove(el)

user_set = set(user_list)
print(list(user_set))
