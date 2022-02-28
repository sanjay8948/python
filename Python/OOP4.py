#Class variable

class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def cal_circumference(self):
        return 2*Circle.pi*self.radius

    def cal_area(self):
        return Circle.pi*self.radius**2


c=Circle(4)

print(c.cal_circumference())

print(c.cal_area())
