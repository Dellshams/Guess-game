import string
import random

print("Welcome to the Guessing Game ")

Stage = input("Choose between Stages Easy, Medium and Hard: \n")

if Stage == "Easy":
    print("You are playing the Easy stage ")

    secret_num = 3
    guess = 0
    guess_count = 0
    guess_limit = 6
    out_of_guesses = False

    while guess != secret_num and not out_of_guesses:
        if guess_count < guess_limit:
            guess = int(input ("Guess a number between 1 and 10: \n"))
            if guess == secret_num:
                break
            elif guess > 10:
                print("Out of guessing range")
            guess_count += 1
            guesses = guess_limit - guess_count
            print ("That was wrong")
            print("You have " + str(guesses) + " guesses left")
        else:
            out_of_guesses = True
            break

    if out_of_guesses:
        print("Game over")
    else:
        print("You got it right!")

elif Stage == "Medium":
    print("You are playing the Medium stage ")

    secret_num = 15
    guess = 0
    guess_count = 0
    guess_limit = 4
    out_of_guesses = False

    while guess != secret_num and not out_of_guesses:
        if guess_count < guess_limit:
            guess = int(input ("Guess a number between 1 and 20: \n"))
            if guess == secret_num:
                break
            elif guess > 20:
                print("Out of guessing range")
            guess_count += 1
            guesses = guess_limit - guess_count
            print ("That was wrong")
            print("You have " + str(guesses) + " guesses left")
        else:
            out_of_guesses = True
            break

    if out_of_guesses:
        print("Game over")
    else:
        print("You got it right!")

elif Stage == "Hard":
    print("You are playing the Hard stage ")

    secret_num = 37
    guess = 0
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    while guess != secret_num and not out_of_guesses:
        if guess_count < guess_limit:
            guess = int(input ("Guess a number between 1 and 50: \n"))
            if guess == secret_num:
                break
            elif guess > 50:
                print("Out of guessing range")
            guess_count += 1
            guesses = guess_limit - guess_count
            print ("That was wrong")
            print("You have " + str(guesses) + " guesses left")
        else:
            out_of_guesses = True
            break

    if out_of_guesses:
        print("Game over")
    else:
        print("You got it right!")


