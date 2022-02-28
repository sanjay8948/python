#zip() function

#user_id=['user1','user2','user3']
#names=['harshit','mohit','rohit']

#user_id=['user1','user2']
#names=['harshit','mohit','rohit']

#user_id=['user1','user2','user3']
#names=['harshit','rohit']

#user_id=['user1','user2','user3']
#names=['harshit']

#print(list(zip(user_id,names)))
#print(tuple(zip(user_id,names)))
#print(dict(zip(user_id,names)))
#print(set(zip(user_id,names)))

user_id=['user1','user2','user3']
names=['harshit','mohit','rohit']
last_name=['kumar','viswas','rastogi']

print(list(zip(user_id,names,last_name)))
print(tuple(zip(user_id,names,last_name)))
#print(dict(zip(user_id,names,last_name))) #not allowed in dictionary because dict take only two argument.
print(set(zip(user_id,names,last_name)))
