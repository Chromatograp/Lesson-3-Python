from typing import List

a = float(input('Напишите первое число'))
b = float(input('Напишите второе число'))

def my_div(a, b):
     if b == 0:
         raise ZeroDivisionError
     return a / b


 try:
     my_div(a, b)
 except ZeroDivisionError as exc:
     print('На ноль делить нельзя')
 else:
     print(my_div(a, b))


 def user_info(last_name, first_name, birth_number, birht_month, birth_year, city, email, phone):
     print(
         f'{last_name} {first_name}, дата рождения {birth_number}.{birht_month}.{birth_year}, город {city}, электронная почта {email}, телефон {phone}')


 c = str(input('Фамилия'))
 d = str(input('Имя'))
 e = int(input('Число рождения'))
 l = int(input('Месяц рождения'))
 m = int(input('Год рождения'))
 f = str(input('Город'))
 g = str(input('Почта'))
 k = int(input('Телефон'))

 user_info(last_name=c, first_name=d, birth_number=e, birht_month=l, birth_year=m, city=f, email=g, phone=k)
 from unittest import result

 n = float(input('Напишите число'))
 o = float(input('Напишите число'))
 p = float(input('Напишите число'))

 def my_f(n, o, p):
     if n > p and p > o:
         result = p + n
         return result
         print(result)
     elif n > p and o > p:
         result = n + o
         return result
         print(result)
     else:
         result = n + p
         return result
         print(result)

 x = my_f(n, o, p)

 print('x =', x)

 x = int(input('Введите положительное число'))
 y = int(input('Введите отрицательное число'))

 def my_func(x, y):
     return(x ** y)

 print(my_func(x, y))

 z = int(input('Введите положительное число'))
 q = int(input('Введите отрицательное число'))

 def my_func(z, q):
    result = 1
    for i in range(abs(q)):
        result *= z
    if q >= 0:
        return result
    else:
        return 1 / result

print(my_func(z, q))

t = str(input("Введите числа в строку, разделив пробелом. $ для выхода из программы"))
number = t.split()
print(number)

def t(*args):
    result = sum(args)
    return result
print(result)


