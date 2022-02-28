from functools import wraps
def print_func_data(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f'you are calling {function.__name__} function')
        print(f'{function.__doc__}')
        return function(*args,**kwargs)
    return wrapper


@print_func_data
def add(a,b):
    '''this function tades two numbers as argument and return their sum'''
    return a+b

print(add(4,9))
        
