#QUESTION 1
def add(num1, num2):
    result = float(num1) + float(num2) 
    return(print(f"Answer is: {result}")) #This function adds the two inputed numbers

def subtract(num1, num2):
    result = float(num1) - float(num2)
    return(print(f"Answer is: {result}")) #This function subtracts the two inputed numbers

def multiply(num1, num2):
    result = float(num1) * float(num2)
    return(print(f"Answer is: {result}")) #This function multiplies the two inputed numbers

def divide(num1, num2):
    result = float(num1) / float(num2)
    return(print(f"Answer is: {result}")) #This function dividess the two inputed numbers

while True:
    try:
        opr = input("Which operation do you want to perform:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\t\t")
        if opr == "1":
            num1 = input("Enter first number: ") #collects input for first number
            num2 = input("Enter second number: ")#collects input for second number
            add(num1, num2)#calls the add function
        elif opr == "2":
            num1 = input("Enter first number: ")#collects input for first number
            num2 = input("Enter second number: ")#collects input for second number
            subtract(num1, num2)#calls the subtract function
        elif opr == "3":
            num1 = input("Enter first number: ")#collects input for first number
            num2 = input("Enter second number: ")#collects input for second number
            multiply(num1, num2)#calls the multiply function
        elif opr == "4":
            num1 = input("Enter first number: ")#collects input for first number
            num2 = input("Enter second number: ")#collects input for second number
            divide(num1, num2)#calls the divide function
        elif opr == "5":
            print("Thank you for using Basic Calculator.") #prints a thank you message and breaks
            break
        else:
            print("Invalid input. Try again")
    except Exception as E:
        print("Error. Try again later")#prints in case of error








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