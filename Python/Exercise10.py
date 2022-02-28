#list comprehension

def num_to_string(l):
    return [str(i) for i in l if type(i)==int or type(i)==float]


l1=input("enter a list:").strip(",")
l2=[]
for i in l1:
     l2.append(i)
print(l2)

