print('Задача 6.')

c = []
while True:
    c = input("Введите числа в строку, разделив пробелом. s для выхода из программы: ")
    c = c.split()
    if 's' in c:
        break
    # c += 1

print(c)

c = map(int, c)
print(sum(c))
