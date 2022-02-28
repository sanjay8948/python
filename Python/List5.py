#Filter even odd
def filter_even_odd(l):
    odd_num=[]
    even_num=[]
    for i in l:
        if i%2==0:
           even_num.append(i)
        else:
           odd_num.append(i)
    return [even_num,odd_num]


list1=[1,2,3,4,5,6,7,8,9,10]
print(filter_even_odd(list1))

#print(min(list1))
#print(max(list1))