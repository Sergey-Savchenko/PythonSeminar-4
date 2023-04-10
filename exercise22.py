# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

from random import randint
numb1 = int(input('Введите количество элементов первого массива: '))
numb2 = int(input('Введите количество элементов второго массива: '))
massiv1 = []
massiv2 = []
for i in range(numb1):
    massiv1.append(int(input(f"Введите {i+1} элемент первого массива: ")))
for i in range(numb2):
    massiv2.append(int(input(f"Введите {i+1} элемент второго массива: ")))
print(massiv1)
print(massiv2)
massiv_result = []
check=False
for i in range(len(massiv1)):
    for j in range(len(massiv2)):
        check=False
        for k in range(len(massiv_result)):
            if massiv1[i]==massiv_result[k]:
                check=True
        if massiv1[i]==massiv2[j] and check==False:
            massiv_result.append(massiv1[i])
# print(massiv_result)
massiv_result.sort()
print(massiv_result)

# massiv1 = [randint(1,numb1) for i in range (numb1)]
# massiv2 = [randint(1,numb2) for i in range (numb2)]