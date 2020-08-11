class Person:
    number_of_people = 0; #class atribute, its shared by all objects

    def __init__(self, name): 
        self.name = name;
        # Person.number_of_people += 1
        Person.add_person()

    @classmethod # decorator 
    def number_of_people_(cls): #class method. It acts on the class itself
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Tim")
p2 = Person("Jim")

print(Person.number_of_people_())