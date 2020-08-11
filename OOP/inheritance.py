
class Pet: 

    def __init__(self, name, age): 
        self.age = age;
        self.name = name;

    def salute(self):
        print("Hello")

class Cat(Pet): #Inherites from pet

    def __init__(self, name, age, color): 
        super().__init__(name, age) #references the super class and calls init with the attributes
        self.color = color;

    def speak(self):
        print("Meow")

class Dog(Pet):

    def speak(self):
        print("Bark")
        

whiskers = Cat("Whiskers", 6, "brown");
whiskers.salute()
whiskers.speak()

