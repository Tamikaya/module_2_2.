first = int(input('Введите число №1: '))
second = int(input('Введите число №2: '))
third = int(input('Введите число №3: '))
if first == second == third: # все числа равны между собой
    print('3')
elif first == second or first == third or second == third: # хотя бы 2 из 3 введённых чисел равны между собой
    print('2')
else: # равных чисел среди 3-х вообще нет
    print('0')




