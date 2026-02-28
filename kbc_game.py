#Kaun Banega Crorepati Game

print("Welcome To Kaun Banega Crorepati !")

# Game Instructions
print("\n\n      Game Structure :-\n(1.) The game consists of 15 questions.\n(2.) Each question has four options (A, B, C, D).\n(3.) Only one option is correct.\n(4.) Prize money increases with each correct answer.")

print("\n      Rules for Answering :-\n(1.) The contestant must choose one option only.\n(2.) Once the answer is locked, it cannot be changed.\n(3.) If the answer is correct, the contestant moves to the next question.\n(4.) If the answer is wrong, the game ends.")

print("\n      Safe (Milestone) Levels :-\n(1.) Certain questions are guaranteed money levels.\n(2.) If the contestant answers a question incorrectly after crossing a safe level, they will receive the amount of the last safe level crossed.\n(3.) First safe level is at question number 4 for ₹10,000 and another safe level is at question number 9 for ₹3,20,000.")

print("\n      Quitting the Game :-\n(1.) The contestant can choose to quit the game at any point before answering a question.\n(2.) The contestant will take home the amount won up to the last correct answer.")

print("\n\nBefore continuing please confirm that you have read the instructions.")

# Confirming that player had read all the instructions 
def readInstructions():
    boolInstructions = input("Enter Yes/No : ")
    if (boolInstructions.lower() == "yes"):
        print("\nSure! Let's proceed towards the game.\n")
    elif (boolInstructions.lower() == "no"):
         print("\nBefore proceeding you have to first read all the instructions carefully.")
         readInstructions()
    else:
         print("\nInvalid Input!")
         print("\nBefore continuing please confirm that you have read the instructions.")
         readInstructions()

readInstructions()

# Initialing the game setup
question_number = 0

prize_amount = ("1,000", "2,000", "5,000", "10,000", "20,000", "40,000", "80,000", "1,60,000","3,20,000", "6,40,000", "12,50,000", "25,00,000", "50,00,000", "1,00,00,000", "7,00,00,000")

question1 = ("Q1. Which blood group is known as the universal plasma donor?", "A. AB+", "B. O−", "C. AB−", "D. O+", "A")

question2 = ("Q2. Which element has the highest electrical conductivity at room temperature?", "A. Copper", "B. Silver", "C. Gold", "D. Aluminium", "B")

question3 = ('Q3. The term “Ceteris Paribus” is most commonly used in which discipline?', "A. Sociology", "B. Economics", "C. Political Science", "D. Psychology", "B")

question4 = ("Q4. Which part of the human brain regulates body temperature and hunger?", "A. Cerebellum", "B. Medulla Oblongata", "C. Hypothalamus", "D. Thalamus", "C")

question5 = ("Q5. Who among the following proposed the Doctrine of Lapse in India?", "A. Lord Canning", "B. Lord Dalhousie", "C. Warren Hastings", "D. Lord Curzon", "B")

question6 = ("Q6. In which year was the first Non-Cooperation Movement formally withdrawn?", "A. 1920", "B. 1921", "C. 1922", "D. 1924", "C")

question7 = ("Q7. Which mathematical constant is represented by Euler’s number?", "A. π", "B. √2", "C. e", "D. φ", "C")

question8 = ("Q8. Which Indian classical dance form originated in the temples of Kerala and was traditionally performed only by men?", "A. Kathakali", "B. Mohiniyattam", "C. Koodiyattam", "D. Manipuri", "A")

question9 = ("Q9. Which constitutional amendment lowered the voting age in India from 21 to 18 years?", "A. 42nd", "B. 44th", "C. 61st", "D. 73rd", "C")

question10 = ("Q10. The Treaty of Purandar (1665) was signed between Shivaji Maharaj and which Mughal general?", "A. Shaista Khan", "B. Raja Jai Singh", "C. Mirza Raja Man Singh", "D. Aurangzeb", "B")

question11 = ("Q11. Which law states that entropy of an isolated system always increases?", "A. Zeroth Law of Thermodynamics", "B. First Law of Thermodynamics", "C. Second Law of Thermodynamics", "D. Third Law of Thermodynamics", "C")

question12 = ("Q12. In linguistics, what does the term “Isogloss” refer to?", "A. A word borrowed from another language", "B. A grammatical rule", "C. A boundary marking linguistic features", "D. A phonetic symbol", "C")

question13 = ("Q13. Who authored the political treatise “Arthashastra”?", "A. Panini", "B. Kalhana", "C. Chanakya (Kautilya)", "D. Banabhatta", "C")

question14 = ("Q14. Which Supreme Court case established the Basic Structure Doctrine of the Indian Constitution?", "A. Golaknath Case", "B. Minerva Mills Case", "C. Kesavananda Bharati Case", "D. Shankari Prasad Case", "C")

question15 = ("Q15. Which mathematical theorem forms the basis of modern public-key cryptography (RSA algorithm)?", "A. Fermat’s Last Theorem", "B. Euler’s Totient Theorem", "C. Pythagoras Theorem", "D. Bayes’ Theorem", "B")

questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14, question15, ]

quit = False

# Checking weather player ready for the question.
def funcReadyQuestion(num):
    readyQuestion = input("Enter Yes/no : ")
    if (readyQuestion.lower() == "yes"):
        print("\nQuestion number",num,"is on your computer screen.\n")
    elif (readyQuestion.lower() == "no"):
         print("\nBefore proceeding you have to confirm that you are ready for the question.\n")
         funcReadyQuestion(num)
    else:
         print("\nInvalid Input!")
         print("\nBefore proceeding you have to confirm that you are ready for the question.\n")
         funcReadyQuestion(num)


# Ask the player for next question
def nextQuestion(num):
    num += 1
    print("Ready for question number",num," for ₹",prize_amount[num-1])
    funcReadyQuestion(num)
    return num
    

# Set the display for the question
def displayQuestion(question):
    print("\n",question[0])
    print(question[1])
    print(question[2])
    print(question[3])
    print(question[4],"\n")
    

# Asking answers from player
def askAnswer(question):
    answer = input("Enter your answer (A-D) or Enter 'E' to quit: ")
    global quit
    
    # To quit
    if (answer.upper() == "E"):
        print("\nAre you Sure that you want to QUIT!!")
        final = input("Enter yes/no : ")
        if (final.lower() == "yes"):
            print("Quitting the Game")
            quit = True
            return False
        elif (final.lower() == "no"):
            print("Then answer the question!!")
            return askAnswer(question)
        else:
            print("Invalid Input!! \nAnswer the question.")
            return askAnswer(question)
    
    # Lock the question
    else : 
        print("\nDo you want to lock your answer?")
        lock = input("Enter lock/no : ")
        if (lock.lower() == "lock"):
            if (answer.upper() in ["A","B","C","D"]):
                if (answer.upper() == question[5]):
                    print("\nAwesome! That's the correct answer.")
                    return True
                else:
                    print("\nSorry! That's a wrong answer.\nYou have to leave this game here only")
                    return False
            else :
                print("\nInvalid Input!\n")
                return askAnswer(question)
            
        elif (lock.lower() == "no"):
            print("\nEnter your final answer!\n")
            return askAnswer(question)
        
        else:
            print("\nInvalid Input!\n")
            print("Enter your final answer!\n")
            return askAnswer(question)
    


take_home = "0"

# Running Question Loop
for i in range(0,15):
    question_number = nextQuestion(question_number)
    displayQuestion(questions[i])
    flag_question = askAnswer(questions[i])
    if (flag_question):
        amount = prize_amount[i]
        if (question_number == 15):
            print("Boom! \nCongratulations!!!!!!!! You Won the game and finally won ₹ 7 crore.")
        elif (question_number == 4):
            print("You won ₹",amount,".\n")
            take_home = "10,000"
        elif (question_number == 9):
            print("You won ₹",amount,".\n")
            take_home = "3,20,000"
        else :
            print("You won ₹",amount,".\n")
        
    else:
        if (quit):
            if i == 0:
                print("You quit early. You won ₹0.")
                break
            else:
                print("Congratulations!!! The final amount you won is ₹", prize_amount[i-1])
                break
        else :
            if (i == 0):
                print("Sorry!! You won ₹0 this time. Better luck next time.")
                break
            else:
                print("The final amount you take to your home is ₹",take_home)
                break
            


