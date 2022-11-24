# 3.Напишите программу, которая принимает на вход координаты точки
#  (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка.
#
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 4


x = int(input("введите координату x: "))
y = int(input("введите координату y: "))

if (x * y == 0):
    quart_num = 0
elif (x > 0 and y > 0):
    quart_num = 1
elif (x < 0 and y > 0):
    quart_num = 2
elif (x < 0 and y < 0):
    quart_num = 3
else:
    quart_num = 4

print(f'Точка с координатами', [x, y], ' находится ')
if (quart_num == 0):
    print('на одной из осей координат')
else:
    print(f'в ', quart_num, '-й четверти')
print()
print('- x=', x, '; y=', y, ' ->', quart_num)
