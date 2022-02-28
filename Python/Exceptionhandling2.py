#else and finally clause in exception handling.


while True:
    try:
        number=int(input("Enter a number: "))
        break
    except ValueError:
        print("Please type integer!!")
    except:
        print("Unexpected error !!!")
    else:
        print(f"user input {number}")
    finally:
        print("Finally blocks.........")
