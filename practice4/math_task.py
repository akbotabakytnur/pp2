import math

# 1

degree = float(input("degree: "))
radian = degree * math.pi / 180
print("radian:", radian)

# 2.

height = float(input("Height: "))
base1 = float(input("Base, 1: "))
base2 = float(input("Base, 2: "))
area = (base1 + base2) * height / 2
print("area:", area)

# 3
n = int(input("number of sides: "))
side = float(input("length of a side: "))
area = (n * side ** 2) / (4 * math.tan(math.pi / n))
print("area:", area)
#4

base = float(input(" base: "))
height = float(input("height: "))
area = base * height
print("area:", area)