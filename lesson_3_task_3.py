print('Задача 3.')

def function(var_1, var_2, var_3):
    """
    Функция отсекает минимальное число из введенных и возвращает сумму оставшихся:
    :param var_1: Переменная 1
    :param var_2: Переменная 2
    :param var_3: Переменная 3
    """
    list = [var_1, var_2, var_3]
    try:
        list.remove(min(list))
        print('Сумма двух наибольших чисел:', sum(list))
    except TypeError:
        print('Введите числа!')

print(function(int(input('Введите число: ')), int(input('Введите число: ')), int(input('Введите число: '))))
