# Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nOperations :-\n1 → Addition\n2 → Subtraction\n3 → Multiplication\n4 → Division\n")

choice = int(input("Enter the number corresponding to the operation : "))

if choice==1:
    print("Sum =", num1+num2)
elif choice==2:
    print("Difference =", num1-num2)
elif choice==3:
    print("Product =", num1*num2)
elif choice==4:
    if num2==0:
        print("Division by 0 is not possible.\nZeroDivisionError")
    else:
        print("Division =", num1/num2)
else:
    print("Invalid Choice")
