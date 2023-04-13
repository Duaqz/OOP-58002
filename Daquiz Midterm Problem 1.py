class Circle():
    def __init__(self, rad, pi,):
        self.__pi = pi
        self.__rad = rad

    def area(self):
        return self.__pi * self.__rad ** 2

    def prmtr(self):
        return self.__pi * self.__rad * 2

    def dsply(self):
        print("Circle Area: ", self.area())
        print("Circle Perimeter: ", self.prmtr())

circle = Circle(float(input("Enter your Radius: ")), 3.14159265359)
circle.dsply()
