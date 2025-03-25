# Create function for addition
def addition():
    result = num1 + num2 

    # Open file equations_task.txt.
    with open("equations_task.txt", "a") as file:
        # Write result to file.
        file.write(f"\n{num1} + {num2} = {result}")

    # Print result to user.
    print(f"\n{num1} + {num2} = {result}\n")

# Create function to subract
def minus():
    result = num1 - num2

    # Open file, write data to file.
    with open("equations_task.txt", "a") as file:
        file.write(f"\n{num1} - {num2} = {result}")

    # Print result to user.
    print(f"{num1} - {num2} = {result}\n")

# Create function to multiply
def multiply():
    result = num1 * num2

    # Open file, write data to file.
    with open("equations_task.txt", "a") as file:
        file.write(f"\n{num1} * {num2} = {result}")

    # Print result to user.
    print(f"{num1} * {num2} = {result}\n")

# Create function to divide
def divide():

    # Try block to catch error.
    try:
        result = num1 / num2

        # Open file, write data to file.
        with open("equations_task.txt", "a") as file:
            file.write(f"\n{num1} / {num2} = {result:.2f}")

        # Print result to user.
        print(f"{num1} / {num2} = {result:.2f}\n")

    # Exception to catch dividion by zero error.
    except Exception:
        print("Zero division error!\nCannot divide by 0\n")

#Loop for user
while True:
    print("Welcome to the program. What would you like to do ?")
    option=input("\nEnter '1' to perfom a calculation\nEnter '2' to view previous calculations\nEnter 'q' to quit\nEnter your choice here: ")
    try:
        if option == '1':
            try:
                num1=float(input("Please enter your first number: "))
                operation=input("Please chose an operator ('+' to add), ('-' to minus), ('/' to devide), ('*' to multiply)\nEnter your choice here: ")
                if operation in ("+", "-", "*", "/"):
                    try:
                        num2 = float(input("Please enter your second number: "))
                        print()

                        if operation == '+':
                            addition()

                        elif operation == '-':
                            minus()

                        elif operation == '/':
                            divide()

                        elif operation == "*":
                            multiply()

                    except ValueError:
                        print("Invalid entry. Please try again:\n")
                else:
                    print("Invalid operator. Please choose from the given operators. ")
            
            except ValueError:
                print("Invalid entry. Please enter a number...")

        elif option == '2':
            try:
                with open("equations_task.txt", "r") as file:
                    print("Previous equations:\n")

                    for line in file:
                        print(line.strip())
                        print()
            except FileNotFoundError:
                print("File does not exist!")

        elif option == 'q' :
            print("You have ended the program. Goodbye!")
            break 

        else:
            print("Invalid entry. Please choose from the options provided...")

    except Exception:
        print("Invalid entery. Please select entry from the options provided...")        
        