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
def next_action():
    print("\nWhat do you want to do next?")
    print("1 → Change operation")
    print("2 → Change numbers")
    print("3 → Exit")
    while True:
        try : 
            repeat = int(input("\nEnter your choice: "))
        except ValueError:
            print("Try entering either of 1/2/3: ")
            continue
        
        if repeat in [1,2,3]:
            return repeat
        else:
            print("Enter a valid choice!!\n")


# Running the main loop
exit_program = False

while True:
    num1 = get_number("first")
    num2 = get_number("second")
    while True:
        operation = get_operation()
        result = perform_calc(num1, num2, operation)
        print(result)
        
        choice = next_action()
        if choice==3:
            exit_program = True
            break
        elif choice==2:
            break
    if exit_program:
        break
        

print("Program Ended!!!")
