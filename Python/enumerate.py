#simply
names=['sanjay','sachin','adarsh','jimmy']
pos=0
for name in names:
    print(f'{pos}----> {name}')
    pos+=1

#enumerate() function
for pos,name in enumerate(names):
    print(f'{pos}----> {name}')

#find position in list
def find_pos(l,target):
    for pos,name in enumerate(l):
        if name==target:
            return pos
    return "not present in list"   



t=input('enter the target:')
print(find_pos(names,t))
