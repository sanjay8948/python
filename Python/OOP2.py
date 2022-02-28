#Instance method

class Person:
    def __init__(self,first_name,last_name,age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def full_name(self):
        return f'{self.first_name} {self.last_name}'

p1=Person('Sanjay','kumar',21)
p2=Person('Nisha','Kumari',27)

#print(p1.full_name())
      #or
print(Person.full_name(p1))

print(p2.full_name())




l=[1,2,3]

#l.clear()
#list.clear(l)

#print(l) 

#l.append(10)
list.append(l,10)

print(l)
