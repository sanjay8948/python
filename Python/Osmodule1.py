import os
import shutil
os.chdir(r'E:\Nahane ka pics\Movies')
#print(os.listdir())
fileiter=os.walk(r'E:\Nahane ka pics')
#for current_path,folder_name,file_name in fileiter:
#    print(f'current path : {current_path}')
#    print(f'folder name : {folder_name}')
#    print(f'file name : {file_name}')

#os.rmdir('new') #ye kewal empty folder ko delete karta h.
#os.makedirs('new\movies') #folder de ander folder banana.

#agar hame aise folder ko delete karna h jo empty nhi h to import shutil module.
#shutil.rmtree('new') #yah permanently delete kar dega recycle bin me nhi jayega.

#shutil.copytree(r'E:\Nahane ka pics\Movies','mm/Movies') #folder ko copy karna kisi folder me.
#shutil.copy('nn.txt','nn.txt/Movies')
#shutil.move()


