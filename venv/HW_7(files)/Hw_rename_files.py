# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного
# имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
#
# 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
import os


def group_renaming(folder_name: str, final_name: str, count_seq_num: int, original_extension: str, final_extension: str,
                   source_name_range: list):
    """
    Групповое переименование файлов в указанной папке текущей директории
    :param folder_name:
    :param final_name:
    :param count_seq_num:
    :param original_extension:
    :param final_extension:
    :param source_name_range:
    :return:
    """

    directory_path = fr"{os.getcwd()}\{folder_name}"
    count = 0
    for i, files in enumerate(os.listdir(directory_path), 1):
        *first_part, extension = files.split(".")

        if ("." + extension) == original_extension:
            a = count_seq_num - int(len(str(count)))
            source_filename = ''.join(first_part)
            count += 1
            my_path = os.path.join(fr"{directory_path}\{files}")

            new_name = f"{source_filename[source_name_range[0]:source_name_range[1]]}{final_name}_{a * '0'}{count}{final_extension}"
            os.rename(fr"{my_path}", fr"{folder_name}\{new_name}")

if __name__ == "__main__":
    group_renaming("files_for_hw_task", "_new_f", 2, ".jpg", ".jpg", [0, 6])
