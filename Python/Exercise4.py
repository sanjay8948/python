#Number Guessing Game
winning_number=27
user_input=input("guess a number b/w 1 to 100:")
if(int(user_input)==winning_number):
    print("YOU WIN!!!")
elif(int(user_input)<winning_number):
    print("too low")
else:
    print("too high")