# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this onl# We are going to write a program that generates a random number and asks the user to
# guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower
# number please”. Similarly, if the user’s guess is too low, the program prints “higher
# number please” When the user guesses the correct number, the program displays the
# number of guesses the player used to arrive at the number.
import random
def game():
    my_num=random.randint(1,100)
    i=1
    print("\t computer choosed 1 number for you, and you have to guess it\n \t \t lets start")
    n=int(input("please enter number of your choice : "))
    #repeat until the user guess the right number
    while my_num != n:
        if n < my_num:
            print("Higher number please")
        else:
            print("Lower number please")

        i += 1
        n = int(input("Try again: "))  #  UPDATE n

    print(f"You guessed the correct number {my_num} in {i} chances")


game()







