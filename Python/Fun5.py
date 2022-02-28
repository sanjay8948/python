def greater(num1,num2):
    if num1>num2:
        return num1
    return num2

def new_greatest(x,y,z):
    return greater(greater(x,y),z)


a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
print(f"{new_greatest(a,b,c)} is greater.")