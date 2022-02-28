#write file.
# w,a,r+

#w--> for write(jo pahle likha h wo delete ho jayega so use for empty files only.)
#a--> for write(jo likha h wo delete nhi hoga.)
#r+-->for write but over write kar dega(and for read and write both).

#with open('file1.txt','a')as f:
with open('file1.txt','r+')as f:
    f.seek(len(f.read()))

    f.write("\nPlease do it.")
