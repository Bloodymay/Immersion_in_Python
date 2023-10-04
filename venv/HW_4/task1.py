# Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]
def transposition(matrix: list[list]) -> list[list]:
    """
    Транспозиция матрицы
    :param matrix:
    :return:
    """

    for i in matrix:
        zipped_list = map(list, zip(*matrix))
    return list(zipped_list)

matrix = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
print(transposition(matrix))

