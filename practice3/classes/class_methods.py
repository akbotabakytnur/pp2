#self
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print("Hello, my name is "+self.name)
p1=Person("Emil",18) 
p1.greet() 
#str
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} {self.age}"
p1=Person("Emil",18) 
print(p1)         