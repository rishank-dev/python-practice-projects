# Calculator

# Getting the number
def get_number(x):
    while True:
        try :
            num = float(input(f"Enter {x} number: "))
            return num
        except ValueError:
            print("Enter a valid number!\n")
        

# Getting an operation to perform
def get_operation():
    print("\nOperations :-\n1 → Addition\n2 → Subtraction\n3 → Multiplication\n4 → Division\n")
    while True:
        try : 
            choice = int(input("Enter the number corresponding to the operation : "))
        except ValueError:
            print("Try entering a valid number\n")
            continue
        
        if choice in [1,2,3,4]:
            return choice
        else :
            print("Try entering a valid number!\n")
            

# Performing the calculation 
def perform_calc(num1, num2, choice):
    if choice==1:
        return f"Sum = {num1+num2}"
    elif choice==2:
        return f"Difference = {num1-num2}"
    elif choice==3:
        return f"Product = {num1*num2}"
    else:
        if num2==0:
            return "Division by 0 not possible."
        else:
            return f"Division = {num1/num2}"
    

# Asking to repeat the function
def ask_repeat():
    while True:
        repeat = input("\nEnter 'yes' to repeat or 'no' to quit : ")
        if repeat.lower()=="yes":
            print("\n")
            return True 
        elif repeat.lower()=="no":
            return False
        else:
            print("Invalid Input!\nTry again\n")
            

# Specifying what to repeat
def specify_repeat():
    print("1 → Change operation with same number\n2→ Change the number and operation both")
    while True:
        try : 
            specify = int(input("Enter 1 or 2: "))
        except ValueError:
            print("Enter either 1 or 2!\n")
            continue
        if specify == 1:
            return True
        elif specify == 2:
            return False


# Running the main loop
exit_program = False

while True:
    num1 = get_number("first")
    num2 = get_number("second")
    while True:
        operation = get_operation()
        result = perform_calc(num1, num2, operation)
        print(result)
        if not ask_repeat():
            exit_program = True
            break
        else: 
            if not specify_repeat():
                break
    if exit_program:
        break
        

print("Program Ended!!!")
