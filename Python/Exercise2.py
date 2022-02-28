name,char=input("enter your name & character:").split(",")
print(f"length of your name is {len(name)}")
print(f"character count:{name.strip().lower().count(char.strip().lower())}")