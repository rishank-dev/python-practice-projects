'''
Throughout the project we will use the following referrals:-

1 → Rock
2 → Paper
3 → Scissor

'''


# ••••••••••••• PROJECT START •••••••••••
import random

print("Welcome to Rock-Paper-Scissor Game !!")


# ------- Defined Variables --------
referral = { 
    1 : "Rock",
    2 : "Paper",
    3 : "Scissor"
}


# ------------ Instructions -------------
def instructions():
    print("""
Enter your choice : 
1 → Rock
2 → Paper
3 → Scissor
""")


# -------- Generating a random computer choice ----------
def generate_computer_choice():
    comp = random.choice([1,2,3])
    return comp
    

# ---------- Taking a user choice ------------
def take_user_choice():
    while True:
        try : 
            user = int(input("Enter you choice (1/2/3) : "))
            if user in [1,2,3]:
                return user
            else :
                print("\nTry entering a valid number!\n")
        except ValueError:
            print("\nInvalid Input \nTry entering a valid number!! \n")
        

# ------------ showing the user and computer choices ----------
def show_choice(a,b):
    print(f"You chose {referral.get(a)} and computer chose {referral.get(b)}. \n")


# ------------ Running the game logic -----------
def game_logic():
    comp_choice =generate_computer_choice()
    user_choice = take_user_choice()
    show_choice(user_choice, comp_choice)
    if comp_choice == user_choice:
        print("Its a draw ! \n")
    else:
        if comp_choice==1 and user_choice==2:
            print("Congratulations! YOU WON \n")
        elif comp_choice==1 and user_choice==3:
            print("Sorry! YOU LOSE \n")
        elif comp_choice==2 and user_choice==1:
            print("Sorry! YOU LOSE \n")
        elif comp_choice==2 and user_choice==3:
            print("Congratulations! YOU WON \n")
        elif comp_choice==3 and user_choice==1:
            print("Congratulations! YOU WON \n")
        elif comp_choice==3 and user_choice==2:
            print("Sorry! YOU LOSE \n")
            

# ------------- Play again or quit -------------
def replay_quit():
    while True: 
        replay = input("Enter 'y' to play again or 'n' to quit : ")
        if replay.lower() == 'y':
            return True
        elif replay.lower() == 'n':
            return False
        else:
            print("\nInvalid Input\n")
            
# -------------- Running main loop ------------
def main():
    while True:
        instructions()
        game_logic()
        if not replay_quit():
            print("\nThanks to play this game !!")
            break
            
        
# ------------- Executing the main loop ----------
main()




# ••••••••••••• PROJECT END ••••••••••••••