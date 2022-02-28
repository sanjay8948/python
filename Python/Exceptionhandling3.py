
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        #print("you can not divide a number by zero.")
        print(err)
        
    except TypeError as err:
        #print("Number must be integer or float.")
        print(err)

    except:
        print("Unexpected error")


print(divide(10,3))
        
