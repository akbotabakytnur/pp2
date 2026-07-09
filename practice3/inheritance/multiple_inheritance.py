class Father:
    def drive(self):
        print("can drive")
class Mother:
    def sing(self):
        print("can sing")    
class Child(Father,Mother) :
    pass
s1=Child()
s1.drive()
s1.sing()           