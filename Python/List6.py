#common element find
def common_element(l1,l2):
    output=[]
    for i in l1:
        if i in l2:
            output.append(i)
    return output


list1=[1,2,3,4,5,6,8]
list2=[2,4,6,8,10]
print(common_element(list1,list2))