# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# Полученные имена сохраните в файл

from random import randint

VOWELS = "AEYUIOaeyuio"


def rnd_names():
    name_len = randint(4, 7)
    while True:
        name = ""
        for i in range(name_len):
            name += chr(randint(65, 90))

        for i in name:
            if i in VOWELS:
                return name.capitalize()


def names_to_file(count: int, file_name: str):
    with open(file_name, "a") as f:
        for i in range(count):
            f.write(rnd_names() + "\n")

if __name__ == "__main__":
    names_to_file(10, "random_names.txt")
