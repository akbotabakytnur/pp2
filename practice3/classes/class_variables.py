class Person:
    species = "Human"   # Class variable

    def __init__(self, name):
        self.name = name   # Instance variable

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.species)
print(p2.species)