
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
        #self.complete_specification=f'{self.brand} {self.model_name} and price {self._price}'

    @property
    def complete_specification(self):
        return f'{self.brand} {self.model_name} and price {self._price}'
               #problem second solved.
           

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

print(phone1._price)

#print(phone1.complete_specification()) 

'''here we call fun "complete_specification()" but if we use setter decorator
    @property the we have no need to call this fun we can simply print
    this .'''
print(phone1.complete_specification)
	
