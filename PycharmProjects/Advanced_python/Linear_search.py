def Linear_search(l,n):
    pos=0
    for i in l:
        if i == n:
            a=pos
        pos+=1
    return a

list1=[2,4,5,3,8,1,9,6,0,7]
a=int(input('Enter the value u want to search: '))
print(Linear_search(list1,a))


