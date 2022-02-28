#Dictionary
#Fromkeys method**********************************
#d=dict.fromkeys(['name','age','height'],'unknown')
         #or
#d=dict.fromkeys(('name','age','height'),'unknown')
          #or
#d=dict.fromkeys("abc",'unknown')
          #or
#d=dict.fromkeys(range(1,11),'unknown')
          #or
#d=dict.fromkeys(['name','age'],['unknown','unknown'])

#for i in d.items():
#    print(i)

#print(d)

#get method*****************************************
d={'name':'unknown','age':'unknown'}
#print(d)
#print(d.get('name'))
#print(d.get('names'))

#if 'name' in d:
#if 'names'in d:
#    print('present')
#else:
#    print('not present')

#if d.get('names'):
#    print('present')
#else:
#    print('not present')

#clear/copy method*********************************
#d.clear()
#d1=d
d1=d.copy()
d1.popitem()

print(d)
print(d1)
