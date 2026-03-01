# Number Guessing Game 
import random

# Showing the Intro
def show_intro():
    print("Welcome to Number Guessing Game! \nI am thinking of a number from 0 to 100 (both inclusive). \nTry to guess it! \n")
    
def generate_num():
    computer_num = random.randint(0,100)
    return computer_num

def play():
    num = generate_num()
    while True:
        try:
            user_num = int(input("Enter a number: "))
            if not (0<=user_num<=100):
                print("Enter the number in the valid range.")
                continue
        except ValueError:
            print("Enter a valid number!!")
            continue
            
        if user_num==num:
            print("\nWohooo!!! Correct Guess.\nYou WON the Game.")
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
                
                
def main_loop():
    show_intro()
    play()
    
main_loop()