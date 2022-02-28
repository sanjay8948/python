def greater(num1,num2):
    if num1>num2:
        return num1
    return num2

a=int(input("enter first number:"))
b=int(input("enter second number:"))

print(f"{greater(a,b)} is greater.")