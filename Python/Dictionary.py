#Dictionary
#user={'name':'harshit','age':24}
#print(user)
#print(type(user))

#Dictionary has not index***************************
#print(user['name'])
#print(user['age'])

#Dictionary can store everything
#like number,string,list,dictionary
user_info={

    'name'      :'Sanjay Kumar',
    'age'       :24,
    'fav_movies':['Krrish','Golmaal','Dhamaal','Hera Pheri'],
    'fav_songs' :['aao sunau','laal dupatta','rab kare']
           }
#print(user_info)
#print(type(user_info))
#print(user_info['fav_songs'])

#in keyword in dictionary***************************
#check if keyword exist in dictionary***************
#if 'name' in user_info:
#    print("present")
#else:
#    print("not present")

#Key method*****************************************
#for i in user_info.keys():
#for i in user_info:
#    print(i)

#check if value exist in dictionary*****************
#if 'Sanjay Kumar' in user_info:
#    print("present")
#else:
#    print("not present")

#Value method**************************************
#for i in user_info.values():
#    print(i)

#Item method****************************************
#for i in user_info.items():
#    print(i)

#Pop method*****************************************
#popped_item=user_info.pop('fav_songs')
#print(f"popped item is {popped_item}")
#print(user_info)

#append method**************Mistake*****************
#more_info={'state':'u.p.'}
#user_info.append(more_info)
#print(user_info)

#update method**************************************
more_info1={'state':'u.p.','country':'India','name':'Akhil'}
user_info.update(more_info1)
print(user_info)
#Dictionary in Dictionary***************************
#user_info={
#   'dict1':{
#    'name'      :'Sanjay Kumar',
#    'age'       :24,
#    'fav_movies':['Krrish','Golmaal','Dhamaal','Hera Pheri'],
#    'fav_songs' :['aao sunau','laal dupatta','rab kare']
#           },
#    'dict2':{
#     'name'     :'Akhil',
#     'age'      :2.5,
#     'fav_song' :'punjabi',
#            }
#          }

#print(user_info)
#print(type(user_info))
#print(user_info['dict1'])
#print(user_info['dict2'])
