#even odd filter

n1=int(input("enter starting number:"))
n2=int(input("enter last number:"))

#by normally**************************************************************
#numbers=list(range(n1,n2+1))
#even_nums=[]
#odd_nums=[]
#for i in numbers:
#    if i%2==0:
#        even_nums.append(i)
#    else:
#        odd_nums.append(i)
    
#by list comprehension****************************************************
even_nums=[i for i in range(n1,n2+1) if i%2==0]
odd_nums=[i for i in range(n1,n2+1) if i%2!=0]

print(even_nums)
print(odd_nums)


