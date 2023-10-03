from random import randint
VOWELS = "AEYUIOaeuioy"


def rnd_name():
    """
    Генерирует рандомное имя латинскими буквами(начинается с заглавной и содержит в любом случае 1 гласную)
    в диапазоне от 4 до 7 символов.

    :return:
    """
    name_len = randint(4, 7)
    while True:
        name = ""
        for i in range(name_len):
            name += chr(randint(65, 90))
        for i in name:
            if i in VOWELS:
                return name.capitalize()


def names_to_file(count, file_name):
    """
    Производит запись сгенерированных имен в файл: одно имя - одна строка
    Принимает на вход количество имен на генерацию и запись(int) и имя файла (str)
    :param count:
    :param file_name:
    :return:
    """
    with open(file_name, "a") as f:
        for i in range(count):
            f.write(rnd_name()+"\n")

if __name__ == "__main__":
    names_to_file(5, "random_names.txt")