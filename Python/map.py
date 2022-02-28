
numbers=[1,2,3,4,5]
def square(a):
    return a**2

#simply********************************************************************
new_list=[]
for num in numbers:
     new_list.append(square(num))
    
print(new_list)

#list comprehension********************************************************
square_new=[i**2 for i in numbers]
print(square_new)

#map function**************************************************************
squares=list(map(square,numbers))
print(squares)

#using lambda
squares1=list(map(lambda a:a**2,numbers))
print(squares1)
    






#map function
