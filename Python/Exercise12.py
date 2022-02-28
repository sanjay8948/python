
def avg_finder(*args):
    avg=[]
    for pair in zip(*args):
        avg.append(sum(pair)/len(pair))
    return avg
l0=[2,4,8]
l1=[1,2,3]
l2=[4,5,6]
print(avg_finder(l0,l1,l2))

#by lambda expression
avg_finder=lambda*args:[sum(pair)/len(pair) for pair in zip(*args)]
print(avg_finder(l0,l1,l2))
