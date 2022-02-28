#inheritance

class Phone:   #base/child class
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)

    def full_name(self):
        return f'{self.brand} {self.model_name}'

    def make_a_call(self,number):
        return f'calling {self.number}'

class Smartphone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):

        #two way
        Phone.__init__(self,brand,model_name,price)   #uncommon way

        #super().__init__(brand,model_name,price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera

             
phone=Phone('nokia','1100',1000)
smartphone=Smartphone('nokia','oneplus 5',30000,'6GB','64GB','20MP')


print(phone.full_name())
print(smartphone.full_name() +f' {smartphone._price}')

        

        
