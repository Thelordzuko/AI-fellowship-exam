#QUESTION 1
def add(num1, num2):
    result = float(num1) + float(num2)
    return(print(f"Answer is: {result}"))

def subtract(num1, num2):
    result = float(num1) - float(num2)
    return(print(f"Answer is: {result}"))

def multiply(num1, num2):
    result = float(num1) * float(num2)
    return(print(f"Answer is: {result}"))

def divide(num1, num2):
    result = float(num1) / float(num2)
    return(print(f"Answer is: {result}"))

while True:
    opr = input("Which operation do you want to perform:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\t\t")
    if opr == "1":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        add(num1, num2)
    elif opr == "2":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        subtract(num1, num2)
    elif opr == "3":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        multiply(num1, num2)
    elif opr == "4":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        divide(num1, num2)
    elif opr == "5":
        print("Thank you for using Basic Calculator.")
        break
    else:
        print("Invalid input. Try again")









#QUESTION 2
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break        # break out of loop
    
    num = int(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")








#QUESTION 3
while True:
    age = input("Enter your age (or type exit to quit): ")
    if age == "exit":
        print("Goodbye!")
        break
    
    try:
        if int(age) >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except:
        print("Invalid input")