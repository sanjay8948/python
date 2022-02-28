#decorator
#decorator increase or inhance functionality of a function.
def decorator_func(any_func):
    def wrapper_func():
        print('this is osm function')
        any_func()
    return wrapper_func

#******************************************************************************
def func1():
    print('this is function 1')


def func2():
    print('this is function 2')

func1=decorator_func(func1)
func1()

print('\n')

func2=decorator_func(func2)
func2()
print('\n\n')
#******************************************************************************
#for shortcut we use

@decorator_func
def func1():
    print('this is function 1')


@decorator_func
def func2():
    print('this is function 2')


func1()
print('\n')
func2()


    
















