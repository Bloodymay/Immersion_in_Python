side_a = int(input('Введите длину стороны "а": '))
side_b = int(input('Введите длину стороны "b": '))
side_c = int(input('Введите длину стороны "c": '))

if (side_a + side_b > side_c and side_c + side_b > side_a) and side_c + side_a > side_b:
    print('Треугольник с такими сторонами может существовать')
    if side_a == side_b == side_c:
        print ('Треугольник равносторонний')
    elif (side_a == side_b or side_a == side_c) or side_b == side_c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Такой треугольник существовать не может')