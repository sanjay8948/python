total=0
i=int(input("enter starting number:"))
n=int(input("enter last number:"))
while i<=n:
    print(f"{i}")
    total=total+i
    i+=1
print(f"={total}")