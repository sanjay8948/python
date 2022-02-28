#will discuss three problem in existing.
#then we will solve them using getter,setter decorator.
#solution of problem in next OOP13.py

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=price
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
print(phone1._price)
print(phone1.complete_specification)
