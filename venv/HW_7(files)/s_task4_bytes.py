# Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.
from s_task2_rand_names import rnd_name
from random import randint


def create_files(extension, max_len_name=30, min_len_name=6, min_byte=256, max_byte=4096, qty_file=6):
    """
    Функция создания файлов с указанным расширением
    :param extension:
    :param max_len_name:
    :param min_len_name:
    :param min_byte:
    :param max_byte:
    :param qty_file:
    :return:
    """
    for _ in range(qty_file):
        with open(rnd_name() + extension, 'w') as f:
            f.write(str(bytes([randint(0, 255) for _ in range(randint(min_byte, max_byte))])))


if __name__ == '__main__':
    create_files('.txt')
