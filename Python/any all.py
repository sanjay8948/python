#any all function
numbers=[1,2,3,4,6,7,8]
even=[]
for num in numbers:
    if num%2==0:
        even.append(True)
    else:
        even.append(False)
         
print(even)

#or

print(all([num%2==0 for num in numbers]))
print(any([num%2==0 for num in numbers]))
