
#simple way

def add(a,b):
    return a+b

print(add(2,4))

#by lambda expression

add2=lambda a,b:a+b
print(add2(2,5))

#even odd ****************************************************************

def is_even(a):
    return True if i%2==0 else False

#print(is_even(6))

even=lambda a:a%2==0
print(even(4))

#last character************************************************************
last_char=lambda s:s[-1]
print(last_char("sanjay"))


