def palindrom(x):
    if x==x[::-1]:
        return "palindrom"
    return "not palindrom"

a=input("enter any number or character:")
print(palindrom(a))