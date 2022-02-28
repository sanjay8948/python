#generator comprehension

#list comprehension

#square=[i**2 for i in range(1,11)]

#generator comprehension

#square=(i**2 for i in range(1,11))

#for num in square:
#    print(num)

#print(next(square))
#print(next(square))
#print(next(square))
#print(next(square))



import time
t1=time.time()
#g=(i**2 for i in range(10000000))
l=[i**2 for i in range(10000000)]
t2=time.time()

total_time=t2-t1

print(total_time)
