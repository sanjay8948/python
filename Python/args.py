#intro to args->make flexible fun
#*operator -> *operator takes a tuple

def all_total(*args):
    total=0
    for i in args:
        total+=i
    return total    
print(all_total(1,3,4,6,9,7,5))  

#############################################################################
def add(*args):
    print(args)
    print(type(args))

add(2,3,4,50)
#############################################################################
def total_mul(*args):
    total=1
    for i in args:
        total*=i
    return total

#print(total_mul(1,3,4,5,7))

#args as argument
#list is only one argument so apply * to unpack list.

#print(total_mul([1,2,3,5]))   #wrong

print(total_mul(*[1,2,3,5]))   #correct




    
