#exception handling
#try except else finally

while True:
    try:
        age=int(input('Enter your age: ')) #seven
        break
    except ValueError:
        print("Invalid Input...")
        

if age<18:
    print("you can't play this game.")
else:
    print("you can play this game.")
