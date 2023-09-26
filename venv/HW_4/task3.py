# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


s = 10000
RICHLIMIT = 5_000_000
RICHTAX = 0.9
THREEOPERATIONS = 3
BONUSTHREE = 1.03
FREENDERING = 50
COMMISSIONOUTDROW = 0.015
MINLIMIT = 30
MAXLIMIT = 600


def withdrow_func(withdrow: int) -> int:
    """
    Функция отвечающая за внесение наличных
    :param withdrow:
    :return:
    """

    global s
    if withdrow % FREENDERING == 0:
        s += withdrow
    withdrow_list.append(withdrow)
    return s


def outdrow_func(outdrow: int) -> int | float:
    """
       Функция отвечающая за выдачу наличных
       :param withdrow:
       :return:
       """

    global s

    if outdrow % FREENDERING == 0:
        comission = outdrow * COMMISSIONOUTDROW

    if comission < MINLIMIT:
        comission = MINLIMIT
        s -= (outdrow + comission)
    elif comission > MAXLIMIT:
        comission = MAXLIMIT
        s -= (outdrow + comission)
        if (comission + outdrow) <= s:
            s -= (outdrow + comission)
        else:
            print("На счете недостаточно средств, чтобы покрыть комиссию на снятие!")
    outdrow_list.append(outdrow)
    return s


def rich_taxes(sum: int | float) -> int | float:
    """
    Функция для расчета налога на богатство
    :param sum:
    :return:
    """

    global s
    s *= RICHTAX
    return s


def fourth_operation_tax(sum: int | float) -> int | float:
    """
        Функция для расчета комиссии за каждую третью операцию
        :param sum:
        :return:
    """

    global s
    s *= BONUSTHREE
    return s


withdrow_list = []
outdrow_list = []
balance_list = []
operation_list = {'Снятие': outdrow_list, 'Пополнение': withdrow_list, 'Баланс': balance_list}
count = 0

while True:
    action = input('Введите операцию 1(пополнение),2(снятие), 3(баланс), Иное(выход): ')
    if s >= RICHLIMIT and count == 1:
        rich_taxes(s)
    if count % THREEOPERATIONS == 0 and count != 0:
        fourth_operation_tax(s)
        count = 0
    if action == '1':
        withdrow_func(int(input('Введите сумму пополнения: ')))
        print(f'Balance:  {s}')
        count += 1

    elif action == '2':
        outdrow_func(int(input('Введите сумму снятия ')))
        print(f'Balance:  {s}')
        count += 1
    elif action == '3':
        balance_list.append(s)
        print(f'Balance:  {s}')
    else:
        print('Выход')
        print(f'Выполненные операции: {operation_list}')
        break
