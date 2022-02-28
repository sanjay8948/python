total=0
i=0
number=input("enter any number:")
l=len(number)
while i<l:
    total=total+int(number[i])
    i+=1
print(f"sum of digits are{total}")