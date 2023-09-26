# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}

def kwargs_reverse(**kwargs) -> dict[str, str | int | bool]:
    """
    Разворот набора ключевых аргументов

    """

    dict_of_locals = locals()
    dict_of_variables = list(dict_of_locals.values())[0]
    reverse_variables = {}
    for key, value in dict_of_variables.items():
        reverse_variables[value] = str(key)
    return reverse_variables


print(kwargs_reverse(rev=True, acc="YES", stroka=4))
