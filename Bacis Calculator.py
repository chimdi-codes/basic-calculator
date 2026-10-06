#Ozugbo Chimdi"s Basic Calculator
print(" \n========My Basic Calculator App=========\n")
print(" This is a basic calculator that only performs addition, multiplication, division and subtraction.")

print(" \nStep:\n")

print("1. Enter the first number.")
print("2. Enter the second number.")
print("3. Enter the operator (+, -, *, /).")

while True:
    num1 = float(input("\nEnter the first number: "))
    num2 = float(input("\nEnter the second number: "))
    operator = input("\nEnter your operator (+, -, *, /):")

    if operator == "+":
        print("\nAnswer =", num1 + num2)

    elif operator == "-":
        print("\nAnswer =", num1 - num2)

    elif operator == "*":
        print("\nAnswer =", num1 * num2)

    elif operator == "/":
        if num2 != 0:
            print("\nAnswer =", num1 / num2)
        else:
            print("Math ERROR!! You cannot divide by zero.")

    else:
        print("Invalid operator!")
        continue

    proceed = input(" \nDo you want to continue using the calculator? ").strip().lower()
    
    if proceed == "no":
        print("\nThank you! for using Ozugbo Chimdi's Calculator app.")
        break

