import sys
import math

def check_sum(st1, st2, st3):
    if st1 + st2 < st3:
        print("Числа не могут быть определены как стороны треугольника:\nсумма двух из них меньше третьего")
        sys.exit()

def check_less(st1, st2, st3):
    if (st1 or st2 or st3) <= 0:
        print("Числа не могут быть определены как стороны треугольника:\nНайдена сторона со значением 0 или меньше")
        sys.exit()

try:
    a = int(input("Введите 3 длины сторон треугольника:\n"))
    b = int(input())
    c = int(input())
except:
    print("Введенное значение не может быть определено как сторона треугольник")
    sys.exit()

check_less(a, b, c)
check_sum(a, c, b)
check_sum(a, b, c)
check_sum(c, b, a)

if a == b == c:
    print("ТРЕУГОЛЬНИК РАВНОСТРОННИЙ")
elif a == b or b == c or a == c:
    print("ТРЕУГОЛЬНИК РАВНОБЕДРЕННЫЙ")
else:
    print("ТРЕУГОЛЬНИК РАЗНОСТРОННИЙ")

p = (a + b + c)/2
square = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(square)
