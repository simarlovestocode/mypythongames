
secret_number = 9
i = 0
while i < 3:
    guess = int(input("guess: "))
    i = i + 1
    if guess == secret_number:
        print("you won!")
        break 
else:
    print("you failed!")
    

    








