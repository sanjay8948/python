#filter function
def is_even(a):
    return a%2==0
numbers=[1,2,3,4,6,8,9,0,5]
#print(filter(is_even,numbers))
evens=tuple(filter(is_even,numbers))
evens1=list(filter(is_even,numbers))

print(evens)
print(evens1)

evens2=tuple(filter(lambda a:a%2==0,numbers))
print(evens2)

#we can iterate list and tuple many times
j=1
while(j<5):
    for i in evens2:
        print(i)

    for i in evens2:
        print(i)

    j+=1


#but map and filter object iterate at only once.

