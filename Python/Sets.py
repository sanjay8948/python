#Sets
s={1,2,3,5,6,2,4,5,3}

#l=[1,2,2,4,3,5,5,5,5,7,6,8,9]   #remove duplicate
#print(list(set(l)))

s1=s.copy()

s.add(8)
s.remove(5)
#s.remove(7) #error because not present so use discard.
s.discard(7)
s.discard(2)

for i in s:
    print(i)

print(s1)
print(s)

s2={5,6,8,3,9}

print(s1|s2)
print(s1&s2)