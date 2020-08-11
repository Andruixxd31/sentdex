class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method of the class dog
    def bark(self):
        print("Bark!")
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age    


d = Dog("Sir pup", 3) #new instance of the class dog, d is a type dog
print(type(d))
d.bark()
print(d.name) #accesing the name 
d.name = "Fluffles" #setting an attribute
print(d.name)
print(d.get_name())
d.set_name("Wuffy")
print(d.get_name())
