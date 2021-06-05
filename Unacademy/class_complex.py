
class ComplexNumber:
    real = 0  # class variables
    img = 0

    def __init__(self, real = 1, img = 1): # dafault values
        self.real = real
        self.img = img
    
    def display(self):
        if self.img >= 0:
            print(f"{self.real} + i{self.img}")
        else:
            print(f"{self.real} - i{-self.img}")

    def conjugate(self):
        self.img *= -1
    
    def modulus(self):
        return self.real*self.real + self.img*self.img
    
    def negative(self):
        self.real *= -1
        self.img *= -1

    def add(self, c2):
        self.real += c2.real
        self.img += c2.img

    def subtract(self, c2):
        self.real += c2.real
        self.img += c2.img
    
    def multiply(self, c2):
        r1 = self.real
        i1 = self.img
        r2 = c2.real
        i2 = c2.img
        self.real = r1*r2 - i1*i2
        self.img = i1*r2 + r1*i2
    
    def divide(self, c2):
        r1 = self.real
        i1 = self.img
        r2 = c2.real
        i2 = -c2.img
        self.real = (r1*r2 - i1*i2)/c2.real*c2.real + c2.img*c2.img
        self.img = (i1*r2 + r1*i2)/c2.real*c2.real + c2.img*c2.img


c1 = ComplexNumber(5, 3) # this calls a class constructor

c1.display()

c2 = ComplexNumber()
c2.display()
print(c1.real)

c1.add(c2)
c1.display()

c1.multiply(c2)
c1.display()

c1.subtract(c2)
c1.display()

c1.divide(c2)
c1.display()

c1.negative()
c1.display()

c1.conjugate()
c1.display()

print(c1.modulus())

# cannot define a function inside a function?
# passed by reference
# when we do self we are refering to the "bucket" where that value is stored?
# is that why list.sort() is defined inside a class and sorted() is a function that returns the list
