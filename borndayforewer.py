"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

'''
year = input('Ввведите год рождения А.С.Пушкина:')
while year != '1799':
    print("Не верно")
    year = input('Ввведите год рождения А.С.Пушкина:')

day = input('Ввведите день рождения Пушкин?')
while day != '6':
    print("Не верно")
    day = input('В какой день июня родился Пушкин?')
print('Верно')
'''
# 1-й способ
f = lambda day: input('В какой день июня родился Пушкин?') != "6"
while f(6) != False: print('Не верно')
print('Верно')
year = lambda year: input("Введите год рождение А.С.Пушкина:") != "1799"
while year(1799) != False: print('Не верно')
print('Верно')

# 2-й способ
def birthday(yearday):
    if yearday == 1:return input("Введите год рождение А.С.Пушкина:") != "1799"
    if yearday == 2: return input('В какой день июня родился Пушкин?') != "6"

while birthday(1): print('Не верно')
while birthday(2): print('Не верно')
