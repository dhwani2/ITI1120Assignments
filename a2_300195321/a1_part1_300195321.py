import math
import random

'''
elementary school quiz function
'''

def elementary_school_quiz(flag, n):
    # Your code for elementary_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    #
    # Preconditions: flag is 0 or 1, n is 1 or 2
    
    # if the user selects 1 for flag
    if (flag == 1):
        # variable for score
        score = 0
        for i in range(n):
            # two rand numbs
            firstNum = random.randint(0, 10)
            secondNum = random.randint(0, 10)
            quesAns = int(input("Answer the following: "+ str(secondNum)+ " - " + str(firstNum) + "= "))
            # if and check for if answer is correct
            if (quesAns == (secondNum - firstNum)):
                print("That is correct")
                score = score + 1
        return score
    # else flag is 2
    else: 
        # variable for score
        score = 0
        for i in range(n):
            # two random ints 
            firstNum = random.randint(0, 10)
            secondNum = random.randint(0, 10)
            quesAns = int(input("Answer the following: "+ str(firstNum)+ "^"+ str(secondNum) + "= "))
            # if and check if the answer is correct 
            if (quesAns == (firstNum**secondNum)):
                print("That is correct")
                score = score + 1
        return score

'''
high school quiz function
'''
def high_school_quiz(a, b, c):
    # Your code for high_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    
    # empty string to store the equation (eqn)
    eqn = ""

    # make sure a, b, and c are not 0
    if (a != 0):
        # insert a for ax^2
        eqn = eqn + str(a) + "x^2"
    # if the b is not 0
    if (b != 0):
        # if b is less than 0, negative sign and greater vice versa
        if (b < 0):
            eqn = eqn + "-" + str(b) + "x"
        else:
            eqn = eqn + "+" + str(b) + "x"
    # check if c is not 0
    if (c != 0):
        # if c is less than 0, negative sign and greater vice versa
        if c < 0:
            eqn = eqn + "-" + str(c)
        else:
            eqn = eqn + "+" + str(c)
    # print the eqn
    print (eqn)

    # calculate the discriminant
    discriminant1 = b*b - 4*a*c
    discriminant2 = math.sqrt(abs(discriminant1))

    # if stmts for the value of the discriminant
    if (discriminant2 > 0):
        print("Real, two roots")
        print((-b + discriminant2)/(2*a))
        print((-b - discriminant2)/(2*a))
    elif (discriminant2 == 0):
        print("Real, one root")
        print(-b/(2*a))
    else:
        print("No real roots")


# main

# your code for the welcome tmessage goes here
print("WELCOME! To the Math Quiz-Generator and Equation Solver.")

# ask for user's name
name=input("What is your name? ")
# enter the schooling level
status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

# if school level is 1
if status=='1':
    # ask subtraction and exponent and how many questions
    flag = int(input("Enter 1 for subtraction and Enter 2 for exponention."))
    n = int(input("Enter how many questions you want to solve"))
    results = elementary_school_quiz(flag, n)
    # if they got a 100%
    if (results == n):
        print("Congratulations ", name, " You’ll probably get an A tomorrow. Goodbye ", name, "!")
    elif (results == n//2):
        print("You did ok ", name, " but I know you can do better. Goodbye ", name, "!")
    elif (n == 0):
        print(" I think you need some more practice ", name,  "Goodbye ", name, "!")


# if schooling level is high school
elif status=='2':

    # your code for welcome message
    print("Welcome to the high school equation solver!")
    flag=True
    
    while flag:
        question=input(name + ", would you like a quadratic equation solved? ")

        # your code to handle varous form of "yes" goes here
        question = question.strip()

        if question == "yes" or question == "Yes" or question == "YES":
            a = int(input("Enter value for a: "))
            b = int(input("Enter value for b: "))
            c = int(input("Enter value for c: "))
            high_school_quiz(a, b, c)
        else:
            flag = False
            
# if they have not selected either option
else:
    print("You have not selected 1 or 2.")

# goodbye print
print("Good bye "+name+"!")

