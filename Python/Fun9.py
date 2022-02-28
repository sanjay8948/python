#function with all type of parameter
#1.parameter 2.*args 3.default parameter 4.**kwargs

def func(name,*args,last_name='unknown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func("harshit",1,2,3,6,8,a=1,b=3)    
