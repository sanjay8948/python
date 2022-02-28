def square(a):
    return a**2
l=[1,2,3,4]

#using predefine function******************************
print(list(map(square,l)))

#using lambda expression*******************************
print(list(map(lambda a:a**2,l)))

#using our function************************************
def my_map(func,l):
    new_list=[]
    for i in l:
        new_list.append(func(i))
    return new_list

print(my_map(square,l))

################################################################################

#using list comprehension

def my_map1(func,l):
    return[func(i) for i in l]
print(my_map1(lambda a:a**2,l))
print(my_map1(square,l))
