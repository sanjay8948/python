def even_generator(n):
    for num in range(1,n+1):
        if num%2==0:
            yield(num)

print(even_generator)


for num in even_generator(20):
    print(num)


def even_generator1(n):
    for num in range(2,n+1,2):
        yield(num)
        
    
print(even_generator1)


for num in even_generator1(20):
    print(num)
