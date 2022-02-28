#can we derive more than one class from base class.
#multilevel inheritance
#method resolution order
##isinstance(),issubclass()

class Phone:   #base/child class
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)

    def full_name(self):
        return f'{self.brand} {self.model_name} and price is{self._price}'

    def make_a_call(self,number):
        return f'calling {self.number}'

class Smartphone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):

        super().__init__(brand,model_name,price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera


class FlagshipPhone(Smartphone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,front_camera):

        super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)
        self.front_camera=front_camera



phone=Phone('nokia','1100',1000)
smartphone=Smartphone('nokia','oneplus5',30000,'6GB','64GB','20MP')
flagshipphone=FlagshipPhone('nokia','oneplus5',30000,'6GB','64GB','20MP','16MP')


print(phone.full_name())
print(smartphone.full_name())
print(flagshipphone.full_name() +f' {flagshipphone.front_camera}')

#print(help(flagshipphone))     #for finding method resolution order.

#isinstance issubclass

#print(isinstance('oneplus5',FlagshipPhone))
#print(isinstance('oneplus5',Phone))
#print(isinstance('oneplus5',Smartphone))
#print(issubclass(FlagshipPhone,Smartphone))
#print(issubclass(FlagshipPhone,Phone))      


