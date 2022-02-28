
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
        #self.complete_specification=f'{self.brand} {self.model_name} and price {self._price}'

    @property
    def complete_specification(self):
        return f'{self.brand} {self.model_name} and price {self.price}'
               
#getter(),setter() python me getter ki jagah hum property decorator use kar sakte h.         

    @property
    def price(self):             
        return self._price
    '''now we can can access price simply by "phone1.price" not need
     of "phone1._price"'''
    
    #@price.setter
    #def price(self,new_price):     ##no effect so check letter
    #     self._price=max(new_price,0) #solution of third problem.
    

    def make_a_call(self,phone_number):
        print(f'calling {phone_number}...')

    def full_name(self):
        return f'{self.brand} {self.model_name}'

    def send_message(self):
        pass # twilio

phone1=Phone('nokia','1100',-1000)
print(phone1.brand)
print(phone1.model_name)

phone1._price=-500      

print(phone1.price)

print(phone1.complete_specification)
