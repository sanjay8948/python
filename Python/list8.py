#simple way

nums=[1,2,3,4,5,6,7,8,9,10]
new_list=[]
for i in nums:
    if i%2==0:
        new_list.append(i*2)
        
    else:
        new_list.append(-i)
#print(new_list)

#list comprehension

new_list1=[i*2 if i%2==0 else (-i) for i in nums]
#print(new_list1)

#nested list comprehension

l=[[1,2,3],[1,3,5],[4,5,6]]
nested_comp=[[i**2 for i in range(1,4)] for j in range(3)]
print(nested_comp)
   
