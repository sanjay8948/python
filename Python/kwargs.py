#kwargs->keyword argument
#**kwargs->double star operator

#kwargs as a parameter
def func_1(**kwargs):
    print(kwargs)
    print(type(kwargs))

func_1(first_name='harshit',last_name='vashistha')

 


#dictionary unpacking

#func_1(**{'first_name':'harshit','last_name':'vashistha'})
