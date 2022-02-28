#list inside a list
def sublist_counter(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count


list1=[1,2,3,[1,2],4,[3,5,8],6,7,[9,12]]
print(sublist_counter(list1))