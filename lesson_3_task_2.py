print('Задача 2.')

def user_info(last_name, first_name, day, month, year, city, email, phone):
    """
    Функция выводит данные о пользователе:
    :param last_name: Фамилия
    :param first_name: Имя
    :param day: Число рождения
    :param month: Месяц рождения
    :param year: Год рождения
    :param city: Место жительства (город)
    :param email: Электронная почта
    :param phone: Номер телефона
    """
    print(
        f'{last_name} {first_name}, дата рождения {day:02d}.{month:02d}.{year}, город {city}, электронная почта {email}, телефон {phone}')

n = str(input('Фамилия: '))
s = str(input('Имя: '))
d = int(input('Число рождения: '))
m = int(input('Месяц рождения: '))
y = int(input('Год рождения: '))
c = str(input('Город: '))
e = str(input('Почта: '))
p = int(input('Телефон: '))

user_info(last_name=n, first_name=s, day=d, month=m, year=y, city=c, email=e, phone=p)
