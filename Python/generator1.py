#generators


#simply
#def nums(n):
#    for i in range(1,n+1):
#        yield(i)

        
#generator
def nums(n):
    for i in range(1,n+1):
        yield(i)
        
print(nums(10))

numbers=nums(10)
print(numbers)
