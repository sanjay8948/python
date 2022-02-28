

students={
    'harshit':{'score':90,'age':24},
    'mohit'  :{'score':75,'age':19},
    'rohit'  :{'score':76,'age':23}
         }
print(max(students,key=lambda item:students[item]['age']))
print(max(students,key=lambda item:students[item]['score']))

print(min(students,key=lambda item:students[item]['age']))
print(min(students,key=lambda item:students[item]['score']))


