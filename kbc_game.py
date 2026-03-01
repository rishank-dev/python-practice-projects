#--------------- KBC Quiz Game -------------------#
print("Welcome To Kaun Banega Crorepati !")



#-------- Module 1: Show instructions ----------#

# Print all instructions
def show_instructions():
    print("\n\n      Game Structure :-\n(1.) The game consists of 15 questions.\n(2.) Each question has four options (A, B, C, D).\n(3.) Only one option is correct.\n(4.) Prize money increases with each correct answer.")
    print("\n      Rules for Answering :-\n(1.) The contestant must choose one option only.\n(2.) Once the answer is locked, it cannot be changed.\n(3.) If the answer is correct, the contestant moves to the next question.\n(4.) If the answer is wrong, the game ends.")
    print("\n      Safe (Milestone) Levels :-\n(1.) Certain questions are guaranteed money levels.\n(2.) If the contestant answers a question incorrectly after crossing a safe level, they will receive the amount of the last safe level crossed.\n(3.) First safe level is at question number 4 for ₹10,000 and the second safe level is at question number 9 for ₹3,20,000.")
    print("\n      Quitting the Game :-\n(1.) The contestant can choose to quit the game at any point before answering a question.\n(2.) The contestant will take home the amount won up to the last correct answer.")
    

# Confirming that player had read all the instructions 
def read_instructions():
    print("\nBefore continuing please confirm that you have read the instructions.")
    while True:
        read = input("Enter Yes/No : ")
        if (read.lower() == "yes"):
            print("\nSure! Let's proceed towards the game.\n")
            break
        elif (read.lower() == "no"):
             print("\nBefore proceeding you have to first read all the instructions carefully.")     
        else:
             print("\nInvalid Input!")
             print("\nBefore continuing please confirm that you have read the instructions.")



#--------- Module 2: Display question ----------#

# Initialing the game setup
question_number = 1

prize_amount = ("0", "1,000", "2,000", "5,000", "10,000", "20,000", "40,000", "80,000", "1,60,000","3,20,000", "6,40,000", "12,50,000", "25,00,000", "50,00,000", "1,00,00,000", "7,00,00,000")

questions = {
    "ques1" : ("Q1. Which blood group is known as the universal plasma donor?", "A. AB+", "B. O−", "C. AB−", "D. O+", "A"),

    "ques2" : ("Q2. Which element has the highest electrical conductivity at room temperature?", "A. Copper", "B. Silver", "C. Gold", "D. Aluminium", "B"),

    "ques3" : ('Q3. The term “Ceteris Paribus” is most commonly used in which discipline?', "A. Sociology", "B. Economics", "C. Political Science", "D. Psychology", "B"),

    "ques4" : ("Q4. Which part of the human brain regulates body temperature and hunger?", "A. Cerebellum", "B. Medulla Oblongata", "C. Hypothalamus", "D. Thalamus", "C"),

    "ques5" : ("Q5. Who among the following proposed the Doctrine of Lapse in India?", "A. Lord Canning", "B. Lord Dalhousie", "C. Warren Hastings", "D. Lord Curzon", "B"),

    "ques6" : ("Q6. In which year was the first Non-Cooperation Movement formally withdrawn?", "A. 1920", "B. 1921", "C. 1922", "D. 1924", "C"),

    "ques7" : ("Q7. Which mathematical constant is represented by Euler’s number?", "A. π", "B. √2", "C. e", "D. φ", "C"),

    "ques8" : ("Q8. Which Indian classical dance form originated in the temples of Kerala and was traditionally performed only by men?", "A. Kathakali", "B. Mohiniyattam", "C. Koodiyattam", "D. Manipuri", "A"),

    "ques9" : ("Q9. Which constitutional amendment lowered the voting age in India from 21 to 18 years?", "A. 42nd", "B. 44th", "C. 61st", "D. 73rd", "C"),

    "ques10" : ("Q10. The Treaty of Purandar (1665) was signed between Shivaji Maharaj and which Mughal general?", "A. Shaista Khan", "B. Raja Jai Singh", "C. Mirza Raja Man Singh", "D. Aurangzeb", "B"),

    "ques11" : ("Q11. Which law states that entropy of an isolated system always increases?", "A. Zeroth Law of Thermodynamics", "B. First Law of Thermodynamics", "C. Second Law of Thermodynamics", "D. Third Law of Thermodynamics", "C"),

    "ques12" : ("Q12. In linguistics, what does the term “Isogloss” refer to?", "A. A word borrowed from another language", "B. A grammatical rule", "C. A boundary marking linguistic features", "D. A phonetic symbol", "C"),

    "ques13" : ("Q13. Who authored the political treatise “Arthashastra”?", "A. Panini", "B. Kalhana", "C. Chanakya (Kautilya)", "D. Banabhatta", "C"),

    "ques14" : ("Q14. Which Supreme Court case established the Basic Structure Doctrine of the Indian Constitution?", "A. Golaknath Case", "B. Minerva Mills Case", "C. Kesavananda Bharati Case", "D. Shankari Prasad Case", "C"),

    "ques15" : ("Q15. Which mathematical theorem forms the basis of modern public-key cryptography (RSA algorithm)?", "A. Fermat’s Last Theorem", "B. Euler’s Totient Theorem", "C. Pythagoras Theorem", "D. Bayes’ Theorem", "B")
}

# Displaying the Question
def ques_display(num,question_data):
    while True:
        print(f"Ready for question number {num} for ₹{prize_amount[num]} ?")
        ready = input("Enter Yes/no : ")
        if (ready.lower() == "yes"):
            print("\nQuestion number",num,"is on your computer screen.\n")
            break
        elif (ready.lower() == "no"):
             print("\nBefore proceeding you have to confirm that you are ready for the question.\n")
        else:
             print("\nInvalid Input!")
             print("\nBefore proceeding you have to confirm that you are ready for the question.\n")
    
    print(f"\n{question_data[0]} \n{question_data[1]} \n{question_data[2]} \n{question_data[3]} \n{question_data[4]} \n")



#------- Module 3: Ask and lock answer -------#

# Ask Answer
def ask_answer(num,question_data):
    while True:
        answer = input("Enter your answer (A-D) or Enter 'E' to quit: ")
        
        # To quit
        if (answer.upper() == "E"):
            print("\nAre you Sure that you want to QUIT!!")
            final = input("Enter yes/no : ")
            if (final.lower() == "yes"):
                print("Quitting the Game")
                return "quit"
            elif (final.lower() == "no"):
                print("Then answer the question!!")
                continue
            else:
                print("Invalid Input!! \nAnswer the question.")
                continue
        
        # Lock the question
        elif answer.upper() in ['A','B','C','D'] :
            while True:
                print("\nDo you want to lock your answer?")
                lock = input("Enter lock/no : ")
                if (lock.lower() == "lock"):
                    if (answer.upper() == question_data[5]):
                        print(f"\nAwesome! That's the correct answer.\n You won ₹{prize_amount[num]}.\n")
                        return True
                    else:
                            print("\nSorry! That's a wrong answer.\nYou have to leave the game here.\n")
                            return False
                elif (lock.lower() == "no"):
                    print("\nEnter your final answer!\n")
                    break
                else:
                    print("\nInvalid Input!\n")
                    print("Enter your final answer!\n")
        else:
            print("\nInvalid Input!\n")
            print("Enter your final answer!\n")




#----------------- Module 4: Quit handling and Prize & milestone tracking ---------------------#

def run():
    for i in range(1,16):
        key = f"ques{i}"
        question_data = questions[key]
        ques_display(i,question_data)
        result = ask_answer(i, question_data)
        
        if result != True:
            if result=="quit":
                print(f"Congratulations!! You will take ₹{prize_amount[i-1]} with you.")
            else:
                if i<=4:
                    print("Sorry, you won ₹0 this time.")
                elif 5 <= i <= 9:
                    print("Congratulations!! You will take ₹10,000 with you.")
                else:
                    print("Congratulations!! You will take ₹3,20,000 with you.")
            break
            
        elif result==True and i==15:
            print("Boom...\nCongratulations!!!!! You won ₹7,00,00,000")
            break
            
            
    
    
#-------------------- MAIN LOOP --------------------#
show_instructions()
read_instructions()
run()

