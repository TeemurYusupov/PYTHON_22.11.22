# 4. Напишите программу, которая будет принимать на вход дробь и
#  показывать первую цифру дробной части числа.

# *Примеры:*
# - 6,78 -> 7
# - 0,34 -> 3


# a=float(input('Введите дробь '))
# b=(a*10)%10
# print(int(b))

string = input('Введите дробное число: ').split(',')[1][0]
print(string)