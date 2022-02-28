class Laptop:
    def __init__(self,name,brand,price):
        self.name=name
        self.brand=brand
        self.price=price
        self.laptop_name=brand+' '+name



    def apply_discount(self,num):
        off_price=(num/100)*self.price
        return self.price-off_price
 
laptop1=Laptop('au114tx','hp',63000)
laptop2=Laptop('apple','macbook pro',230000)

print(laptop1.apply_discount(50))

print(laptop2.apply_discount(50))
