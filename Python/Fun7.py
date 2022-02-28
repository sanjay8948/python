def fibbonacci_seq(x):
    a=0
    b=1
    if x==1:
        print(a)
    elif x==2:
        print(a,b)
    else:
        print(a,b,end=" ")
        for i in range(x-2):
            c=a+b
            a=b
            b=c
            print(b,end=" ")


n=int(input("enter number of term:"))
fibbonacci_seq(n)