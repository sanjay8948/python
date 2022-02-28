#Read & write file.

#open function
#read method
#tell method
#seek method
#readline method
#readlines method
#close method

#f=open(r"C:\Users\h.p\Desktop\New folder\file1.txt") #if u create file on desktop.
f=open('file1.txt')
print(f'cursor position={f.tell()}')

print(f.read())
print(f'cursor position={f.tell()}')

print("before seek method")
f.seek(16)
print("after seek method")
print(f'cursor position={f.tell()}')
print(f.read())
f.close()
