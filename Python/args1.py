#Exercise
def to_power(num,*args):
    if args:
        return[i**num for i in args]
    else:
        return ("you did not pass any args")



nums=[1,2,3]
print(to_power(2,*nums))

#*args does not take dictionary so we use **kwargs for dictionary
