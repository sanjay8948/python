#exception handling
#try except else finally


while True:
    try:
        age=int(input('Enter your age: ')) #seven
        break
    except ValueError:
        print("may be you entered string instead of number,try again.")
    except:
        print("Unexpected error...")
        

if age<18:
    print("you can't play this game.")
else:
    print("you can play this game.")
