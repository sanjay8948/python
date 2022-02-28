#name="sanjay"
#if 'a' in name:
#    print("a is present in name")
#else:
#    print("a is not present in name")

 #*****************
name=input("enter your name:")
ch=input("enter character you want to search:")
if ch in name:
    print(f"{ch} is present in your name")
else:
    print(f"{ch} is not present in your name")