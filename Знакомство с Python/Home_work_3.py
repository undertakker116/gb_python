"""1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах)."""

from random import sample, randint, randrange, uniform
from math import ceil
import numpy as np


def generate_random_list(count):
    """Функция генерации рандомного списка.Количество цифр в списке задает пользователь """

    list_random = sample(range(count * 2), count)
    print(list_random)
    return list_random


def sum_odd_numbers(generate_random_list):
    """Подсчет стоящих на нечётных позициях цифр списка"""
    numbers_sum = 0
    for i in range(1, len(generate_random_list), 2):
        numbers_sum += generate_random_list[i]
    return numbers_sum


if __name__ == '__main__':
    print(sum_odd_numbers(generate_random_list(int(input("enter number: ")))))

"""2. Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д."""


def generate_random_list(length, count):
    """Функция генерации рандомного списка. Количество цифр в списке задает пользователь """

    list_random = [randrange(1, length) for i in range(count)]
    print(list_random)
    return list_random


def multiplication_of_pairs(my_list):
    """Найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д"""
    return [my_list[i] * my_list[-i - 1] for i in range(ceil(len(my_list) / 2))]


if __name__ == '__main__':
    my_list = generate_random_list(length=int(input('Задайте диапазон чисел. Например до 10 или до 100: ')),
                                   count=int(input('Задайте длину списка: ')))
    print(multiplication_of_pairs(my_list))

"""3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк."""


def move_to_bin(num):
    '''Преобразование из десятичной системы в двоичную'''
    numbers = []
    while num >= 1:
        if num % 2 == 0:
            numbers.append(0)
        elif num % 2 == 1:
            numbers.append(1)
        num = num // 2
    num = num // 2
    numbers.reverse()
    return numbers


if __name__ == '__main__':
    print(move_to_bin(int(input("enter number: "))))

"""4.Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов."""


def generate_list(lenght):
    """Функция генерации рандомного списка. Количество цифр в списке задает пользователь """
    my_ls = []
    for i in range(1, lenght):
        my_ls.append(f'{uniform(1, 10):.2f}')
    ls = np.array(my_ls, dtype=float)
    print(ls)
    return ls


def solution(my_list):
    fractional_part = []
    for i in my_list:
        fractional_part.append(f'{float(i) - int(i):.2f}')
    list_nums = np.array(fractional_part, dtype=float)
    maxium = max(list_nums)
    minimum = min(list_nums)
    print(f'Min: {minimum}, max: {maxium} . Difference: {maxium - minimum:.2f}')
    exit()


if __name__ == '__main__':
    my_list = generate_list(int(input('enter number: ')))
    print(solution(my_list))
