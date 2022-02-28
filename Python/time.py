import time

print('this is line one')
x=int(input("enter a number:"))
t1=time.time()
if x==5:
    print('x is equal to 5')
print("x is not equal to 5")    
t2=time.time()
print(t2-t1)
