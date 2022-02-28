#reverse of list

def reverse_list(l):
    #return l[::-1]
          #or
    #l.reverse()
    #return l
      #or
    output=[]
    for i in range(len(l)):
        poped_item=l.pop()
        output.append(poped_item)
    return output

#reverse of string in list

def reverse_elements(l):
    elements=[]
    for i in l:
        elements.append(i[::-1])
    return elements


list1=['1','2','3','4','5','6','7']
print(reverse_list(list1))

list2=['abc','tuv','xyz']
print(reverse_elements(list2))

