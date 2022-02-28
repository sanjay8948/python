class Laptop:
    def __init__(self,name,brand,price):
        self.name=name
        self.brand=brand
        self.price=price
        self.laptop_name=brand+' '+name



laptop1=Laptop('au114tx','hp',63000)
print(laptop1.name)
print(laptop1.laptop_name)
