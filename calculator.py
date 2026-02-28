# Calculator

# Repeat again function
def func_repeat():
    repeat = input("\nEnter 'yes' to repeat or 'no' to quit : ")
    if repeat.lower()=="yes":
        print("\n")
        return 1
    elif repeat.lower()=="no":
        return 2
    else:
        print("Invalid Input!\nTry again\n")
        return func_repeat()

while True:
    try :
        num1 = float(input("Enter first number: "))
    except ValueError:
        print("Enter a valid number\n")
        continue
        
    try : 
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Enter a valid number\n")
        continue

    print("\nOperations :-\n1 → Addition\n2 → Subtraction\n3 → Multiplication\n4 → Division\n")

    while True:
        try : 
            choice = int(input("Enter the number corresponding to the operation : "))
        except ValueError:
            print("Try entering a valid number\n")
            continue
    
        if choice==1:
            print("Sum =", num1+num2)
            break
            
        elif choice==2:
            print("Difference =", num1-num2)
            break
            
        elif choice==3:
            print("Product =", num1*num2)
            break
            
        elif choice==4:
            if num2==0:
                print("Division by 0 is not possible.")
                break
            else:
                print("Division =", num1/num2)
                break
                
        else:
            print("Invalid Choice\nTry again\n")
            continue
        
    var = func_repeat()
    if var==1:
        continue
    else:
        break
        
print("Program Ended!!!")
