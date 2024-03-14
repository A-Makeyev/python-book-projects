from random import randint

print("The computer has chosen a number between 1 to 100, try to guess it")
computer_number = randint(1, 100)
guess_count = 10

user_number = int(input("Try to guess it: "))
guess_count -= 1

while guess_count != 0:
    if user_number == computer_number:
        print("That's right, the number is " + str(computer_number) + " and it took you " + str(guess_count) + " guesses!")
        break
    elif user_number > computer_number:
        if guess_count <= 3:
            user_number = int(input("Too high, you have " + str(guess_count) + " guesses left! Try again: "))
        else:
            user_number = int(input("Too high, try again: "))
        guess_count -= 1
    elif user_number < computer_number:
        if guess_count <= 3:
            user_number = int(input("Too low, you have " + str(guess_count) + " guesses left! Try again: "))
        else:
            user_number = int(input("Too low, try again: "))
        guess_count -= 1

if guess_count == 0:
    print("You're out of guesses!, the number was: " + str(computer_number))
    
exit(0)
