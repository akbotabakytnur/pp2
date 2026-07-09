class Person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print("Hello ",self.name)   
class Student(Person):
    def greet(self):
        print("Hi ",self.name)    
s1=Student("Alice")
s1.greet()             