f=open('file1.txt')
##print(f.readlines())

#lines=f.readlines()
##print(len(lines))

#for line in lines:
#    print(line,end="")


for line in f.readlines()[:2]:
    print(line,end="")


f.close()
