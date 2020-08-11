class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # commonly used to represent objects, useful for debbuging
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # commonly used to show objects to the user
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # overwritting dunder add to add the salaries of employees objects
    def __add__(self, other):
        return self.pay + other.pay

    # overwriting len to work with the employee objects
    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1)  # calls __str__
print(repr(emp_1))  # The same as print(emp_1.__repr__())
print(emp_1 + emp_2)
print("ab" + "cd")
print(len(emp_1))
