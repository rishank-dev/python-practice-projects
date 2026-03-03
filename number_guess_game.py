# Number Guessing Game 
import random


# Showing the Intro
def show_intro():
    print("Welcome to Number Guessing Game!\n")


# Setting the difficulty
def choose_difficulty():
    max_easy = 50
    max_medium = 100
    max_hard = 500
    print("\nChoose a difficulty level:\n1 → Easy (from 0 to 50) \n2 → Medium (from 0 to 100) \n3 → Hard (from 0 to 500) \n")
    while True:
        try:
            level = int(input("Enter level(1/2/3) : "))
        except ValueError:
            print("Invalid Input! \nTry entering a valid number! \n")
            continue
            
        if level in [1,2,3]:
            if level==1:
                print(f"\nI am thinking of a number from 0 to {max_easy} (both inclusive). \nTry guessing it. \nYou will have a total of 7 attempts. \n")
                return max_easy
            elif level==2:
                print(f"\nI am thinking of a number from 0 to {max_medium} (both inclusive). \nTry guessing it. \nYou will have a total of 7 attempts. \n")
                return max_medium
            else:
                print(f"\nI am thinking of a number from 0 to {max_hard} (both inclusive). \nTry guessing it. \nYou will have a total of 7 attempts. \n")
                return max_hard
        else:
            print("Enter a valid number!! \n")


# Generating a random number to be guessed
def generate_num():
    max = choose_difficulty()
    computer_num = random.randint(0,max)
    return computer_num , max


# Playing the game
def play():
    attempts = 0
    max_attempts = 7
    num , max_range = generate_num()
    
    while attempts<max_attempts:
        attempts += 1
        try:
            user_num = int(input(f"Remaining attempts : {(max_attempts+ 1) - attempts} \nEnter a number: "))
            if not (0<=user_num<=max_range):
                print("Enter the number in the valid range.\n")
                continue
        except ValueError:
            print("Enter a valid number!!")
            continue
            
        if user_num==num:
            print(f"\nWohooo!!! Correct Guess.\nYou WON the Game in {attempts} attempts.")
            break
            
        elif user_num<num:
            if num-user_num <= 5:
                print("The number you enter is LOWER than the correct number, but you are VERY CLOSE. \n")
            elif 5< num-user_num <=20:
                print("The number you enter is LOWER than the correct number, but you are CLOSE.\n")
            else:
                print("The number entered by you is TOO LOW.\n")
                
        else:
            if user_num-num <= 5:
                print("The number you enter is HIGHER than the correct number, but you are VERY CLOSE.\n")
            elif 5< user_num-num <=20:
                print("The number you enter is HIGHER than the correct number, but you are CLOSE.\n")
            else:
                print("The number entered by you is TOO HIGH\n")
        
    else:
            print(f"You run out of the total attempts!!!! \nThe correct number was {num}.")


# Ask to play again
def play_again():
    print("\nDo you want to play again?")
    while True:
        replay = input("Enter 'yes' to play again and 'no' to quit : ")
        if replay.lower() == 'yes':
            return True
        elif replay.lower() == 'no':
            return False
        else:
            print("Invalid Input! \n")


# Declaring the main loop in which game is run
def main_loop():
    show_intro()
    while True:
        play()
        if not play_again():
            break

# Running the main loop
main_loop()
