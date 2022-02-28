names=['harshit','raj','lovely','mohit']
print(max(names,key=lambda items:len(items)))
print(min(names,key=lambda items:len(items)))


students=[
    {'name':'harshit','score':90,'age':24},
    {'name':'mohit','score':70,'age':19},
    {'name':'rohit','score':60,'age':23}
         ]
print(max(students,key=lambda item:item.get('score'))['name'])
print(min(students,key=lambda item:item.get('score'))['name'])
