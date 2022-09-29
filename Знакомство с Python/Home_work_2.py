"""1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр."""

num = int(input("enter number: "))
sum_nums = []
while num > 0:
    sum_nums.append(num%10)
    num //= 10
print(sum(sum_nums))
2 вариант

def sum_nums(num):
    return sum(map(int,str(num)))

print(sum_nums(input('enter number: ')))

"""2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N."""
n = int(input('enter number: '))
multiply = 1
list_nums = []
for i in range(1,n+1):
    multiply *= i
    list_nums.append(multiply)
print(f'{n} - {list_nums}')

"""3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму."""

list_nums = [round((1 + 1 / x) ** x, 2) for x in range(1, int(input('enter number: ')) + 1)]
print(sum(list_nums))

"""4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях(не индексах)."""
num = int(input('enter number: '))
numbers = [i for i in range(-num, num + 1)]
multiplication = 1
x = int(input('Enter  position of first element: '))
y = int(input('Enter position of second element: '))
for i in range(len(numbers)):
    mult = numbers[x - 1] * numbers[y - 1]
print(f'Multiplication of elements: {numbers[x - 1]} * {numbers[y - 1]} =', multiplication)

"""5.Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random"""

from random import choice

unsorted_list = [r for r in range(1, int(input('enter number for generate list: ')))]
print(f'До сортировки - {unsorted_list}')
for i in range(len(unsorted_list)):
    n = choice(unsorted_list)
    if n < len(unsorted_list):
        unsorted_list[i], unsorted_list[n] = unsorted_list[n], unsorted_list[i]
print(f'После сортировки - {unsorted_list}')
