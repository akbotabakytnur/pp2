#1
def squares(n):
    for i in range(n+1):
        yield i*i
n=int(input("n:"))  
for square in squares(n):
    print(square)
#2
def numbers(a):
    for i in range(a+1):
        if i%2==0:
            yield i
a=int(input("a:"))
for num in numbers(a):
    print(num,end=",") 
#3
def numbers(b):
    for i in range(b+1):
        if i%3==0 and i%4==0:
            yield i
b=int(input("b:"))            
for num in numbers(b):
    print(num)            
#4
def squares(c, d):
    for i in range(c, d + 1):
        yield i * i

c=int(input("c:"))
d=int(input("d:"))
for num in squares(a, b):
    print(num)
#5
def numbers(x):
    while x>=0:
        yield x
        x=x-1
x=int(input("x:5"))
for num in numbers(x):
    print(num)     