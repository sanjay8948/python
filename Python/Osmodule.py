import os
#print(os.getcwd())  #cwd-current working directories
#os.chdir(r'E:\Nahane ka pics')
#print(os.getcwd())
#os.mkdir('Movies')
#print(os.path.exists('Movies'))
#if os.path.exists('Movies'):
#    print('already exist')
#else:
#    os.mkdir('Movies')

#open('file.txt','a').close()   
#os.mkdir(r'E:\Nahane ka pics\Movies')
#print(os.listdir(r'E:\Nahane ka pics\Movies'))

#for item in os.listdir():
#    print(r'E:\Nahane ka pics'+'\\'+item)

#for item in os.listdir():
#    path=os.path.join(os.getcwd(),item)
#    print(path)

for item in os.listdir(r'E:\Nahane ka pics'):
    path=os.path.join(r'E:\Nahane ka pics',item)
    print(path)
