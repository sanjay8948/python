def decorator_func(any_func):
    def wrapper_func(*args,**kwargs):
        '''this is wrapper function'''
        print('this is osm function')
        return any_func(*args,**kwargs)
    return wrapper_func


@decorator_func
def add(a,b):
    '''this is add function'''
    return a+b

print(add(3,6))

print(add.__doc__)  #because of this name and doc problem we modefied
print(add.__name__) #so see decorator3.py
