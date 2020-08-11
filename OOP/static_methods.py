class Math:

    @staticmethod
    def add5(x): #does not access an instance
        return x + 5

    @staticmethod
    def pr(): #does not access an instance
        print("x")

print(Math.add5(5))

