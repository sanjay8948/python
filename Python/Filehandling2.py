f=open('file1.txt')
#print(f.readline(),end="")
#print(f.readline(),end="")
#print(f.readline())

for line in f:
    print(line,end="")

f.close()
