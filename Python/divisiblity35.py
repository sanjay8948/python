a=int(input("enter any number:"))
if a%3==0:
    if a%5==0 and a%3!=0:
        print("number is divisible by 5 only")
    elif(a%5!=0 and a%3==0):
        print("number is divisible by 3 only")
    else:
        print("number is divisible by both 5 and 3")

elif a%5==0:
    if a%3==0:
        print("number is divisible by 3 only")

    else:
        print("number is divisible by 5 only")

else:
    print("number is neither divisible by 5 nor 3")
   
