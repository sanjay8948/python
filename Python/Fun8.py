def user_info(first_name,last_name,age):
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")

a,b,c=input("enter your first name,last name and age:").split(" ")
user_info(a,b,c)