
def is_up_monotone(X, d):
    """ 
    Returns either 0 or 1.
    @type X: int
    @type d: int
    @rtype: int
    """

    d = int(d)
    test1 = -1
    test2 = -1

    for i in range(0, len(X), d):
        test2 = test1
        test1 = int(X[0 + i : d + i])

        if(test2 > test1):
            return 0

    return 1

def textttis_up_monotone(X, d):
    """
    Returns True or False.
    @type X: int
    @type d: int
    @rtype: bool
    """
    emp1 = ""
    emp2 = -1
    counter = 0
    passed = True

    for i in range(0, len(X), int(d)):
            if (i != len(X) - int(d)):
                print(X[i:i+int(d)], end = ", ")
    
    for i in range(len(X)):
        emp1 = emp1 + X[i]
        counter += 1

        if ((counter) == int(d)):
            if (int(emp1) <= int(emp2)):
                passed = False
                break
            else:
                emp1 = emp2
                emp1 = ""
                counter = 0
    return passed



flag = True
while(flag):

    """
    Greets user.
    Asks user for name, positive integer, and split number.
    Prints whether sequence is or is not up monotone. 
    Calls the textttis_up_monotone function in either case.
    Precondition: name is a string, X and d are positive integers. 
    """

    question = "yes"
    print("***********************\n**\n* Welcome to up_monotone * \n**\n***********************")
    name = input("What is your name? ")
    print("***********************\n**\n* " + name + ", Welcome to up_monotone" + " * \n**\n***********************")
    question=(question.strip()).lower()
    
    while (question == 'yes'):
        x = "-1"
        x2 = True
        d = "-1"
        d2 = True

        condition = True
        flag = True

        while (condition == True):
            question2 = input("\n\n" + name + ", would you like to test if a number admits an up-monotone split of given size: ")
            question2 = (question2.strip()).lower()
            
            if (question2 =='no'):
                exit()
          
            x = input("Enter a positive integer: ")
            if (x.isdigit()):
                x2 = len(x)
            
            else:
                print("The input can only contain a positive integer: ")
                flag = False
                
            d = input("Input the split (The split must divide the length of the inputted integer): ")
            d2 = int(d)
            
            if(d.isdigit() and (x2 % d2)==0):
                condition = False
            else:
                print("Invalid split")
                flag = False
                
        if (flag == True):
            if (is_up_monotone(x, d)):
                print("The sequence is up_monotone")
                textttis_up_monotone(x, d)

            else:
                print("The sequence is not up_monotone")
                textttis_up_monotone(x, d)