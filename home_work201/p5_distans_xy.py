# 2. Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними
# в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


from math import *
print('Введите координаты точки A: ')
x1 = float(input())
y1 = float(input())

print('Введите координаты точки B: ')
x2 = float(input())
y2 = float(input())

Dist = sqrt((x2-x1)**2 + (y2-y1)**2)

print('Расстояние от точки А до точки В равно', round(Dist, 2))
print()
print('- A ',(x1, y1),'; B ', (x2, y2),' ->', round(Dist, 2))