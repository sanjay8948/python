







def max_n(d,n):
    l=sorted(d.values())
    return l[-1:-n-1:-1]
    
    
d1={'a':1,'b':4,'c':25,'d':16}
print(max_n(d1,3))
