print('Задача 6.')

your_list = []
while True:
    # Цикл собирает введенные пользователем списки в один список
    str = (input("Введите числа в строку, разделив пробелом. s для выхода из программы: ")).split()
    your_list.append(str)
    if 's' in str:
        break

un_list = your_list()
for i in list:
    # Цикл распаковывает списки, вложенные в предыдущий список, и собирает из них новый
    un_list += i

un_list.remove('s')
# Удаляем букву, оставив в списке только цифры
un_list = map(int, un_list)
# Переводим цифры в числовой формат
print('Сумма ваших чисел', sum(un_list))
