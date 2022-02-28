
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name

        self._price=max(price,0)
               #or

        #if price >0:                    #1st problem solved
        #    self._price=price
        #else:
        #    self._price=0

        
        self.complete_specification=f'{self.brand} {self.model_name} and price {self._price}'

    def make_a_call(self,phone_number):
        print(f'calling {phone_number}...')

    def full_name(self):
        return f'{self.brand} {self.model_name}'

    def send_message(self):
        pass # twilio

phone1=Phone('nokia','1100',-1000)
print(phone1.brand)
print(phone1.model_name)

phone1._price=-500      #but this is third problem.
                        #solution of this in OOP15.py

print(phone1._price)
print(phone1.complete_specification)


#second problem is value of _price and price of complete_specification not same.
#solution of this in OOP14.py
