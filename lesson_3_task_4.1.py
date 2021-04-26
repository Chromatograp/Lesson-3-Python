print('Задача 4.')

x = int(input('Введите положительное число, x: '))
y = int(input('Введите отрицательное число, y: '))

def my_func(x, y):
    return (x ** y)

print("x^y=%.2f" % (my_func(x, y)))