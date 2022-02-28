class Laptop:
    discount_percent=10
    def __init__(self,name,brand,price):
        self.name=name
        self.brand=brand
        self.price=price
        self.laptop_name=brand+' '+name



    def apply_discount(self):
        off_price=(Laptop.discount_percent/100)*self.price
        return self.price-off_price

#Laptop.discount_percent=25
 
laptop1=Laptop('au114tx','hp',63000)
laptop2=Laptop('apple','macbook pro',230000)

print(laptop1.apply_discount())
print(laptop2.apply_discount())
