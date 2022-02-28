#list of square of element of list

def square_list(l):
    square=[]
    for i in l:
        square.append(i*i)
    return square

#list1=list(range(1,11))
       #or
list1=range(1,11)
print(square_list(list1))
