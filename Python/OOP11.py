#some special naming convention
#Name managing, __name (not a convention)

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.__price=price

    def make_a_call(self,phone_number):
        print(f'calling {phone_number}...')

    def full_name(self):
        return f'{self.brand} {self.model_name}'

    def send_message(self):
        pass # twilio

phone1=Phone('nokia','1100',1000)
#print(phone1.__price)
print(phone1._Phone__price)
phone1._Phone__price=-1000
print(phone1._Phone__price)

#print(phone1.__dict__)

#phone1._price=-1000
#print(phone1._price)
        
