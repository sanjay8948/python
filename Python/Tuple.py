#Tuple


#tuple without paranthesis*************************
books='hindi','english','physics','chemistry','math'
#print(books)
#print(type(books))

#tuple with one element*****************************
#num=1,
#num=(1,)
num=('sanjay',)
#print(num)
#print(type(num))

#tuple unpacking************************************
#songs=('song1','song2','song3')
#a,b,c=songs
#print(a)

# no append,insert,pop,remove***********************
days=('Monday','tuesday','wednesday','thurseday','friday','saterday','sunday')
mixed=(1,2,3,4.0,5)
#print(days)
#print(type(days))
#print(mixed)
#print(type(mixed))

#Index**********************************************
#print(days[0])
#print(days[4])

#Min & Max******************************************
#print(min(mixed))
#print(max(mixed))

#For loop*******************************************
#for i in days:
#    print(i)

#while loop*****************************************
#i=0
#while i<len(days):
#    print(days[i])
#    i+=1

#count**********************************************
#count=0
#for i in days:
#    count+=1
#print(count)

#List inside Tuple**********************************
#name=('Sanjay','Neeraj',[1,3,5,'raj'],'Santosh',['dhoom','dhoom2','dhoom3'],'Sameer','Visnu',)
#print(name)
#popped_item=name[2].pop()
#print(popped_item)
#print(name)
#append_item=name[2].append(input("enter appending element:"))
#print(name)

#Function returning two values**********************
#def func(int1,int2):
#    add=int1+int2
#    mul=int1*int2
#    return add,mul
#a=int(input("enter first number:"))
#b=int(input("enter second number:"))
#print(func(a,b))
#we find output in the form of tuple (add,mul)
#if we want to show result dinstinctly then
#(x,y)=func(a,b)
#print(x)
#print(y)

#somthing more about tuple**************************
#nums=tuple(range(1,11))
#print(nums)
#nums1=list(nums)
#print(nums1)
#nums2=str(nums)
#print(nums2)