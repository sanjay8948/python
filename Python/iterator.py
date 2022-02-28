#iterator vs iterable
numbers=[1,2,3,4,5]
squares=map(lambda a:a**2,numbers)
#for i in numbers:
#    print(i)

number_iter=iter(numbers)

print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))

#print(next(numbers))   #not ietrator

print(next(squares))  #iterator
print(next(squares))
print(next(squares))
