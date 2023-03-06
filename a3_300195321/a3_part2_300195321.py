
"""
QUESTION #1
"""
def sum_odd_divisors(n):
    """
    Takes n as input and returns sum of positive odd divisors of n.
    If n is 0 returns None.
    @type n: int
    @rtype: None
    @rtype: int
    """
    sum = 0
    if (n == 0):
        return None
    else:
        if (n < 0):
            n = -n
        for i in range(1, (n + 1)):
            if (n%i == 0) and (n%2 != 0):
                sum += i
        
    return sum

print(sum_odd_divisors(45))

"""
QUESTION #2
"""
def series_sum(n):
   """
    Takes a non-negative integer and returns the sum of a series
    for the inputted integer. 
    @type n: int
    @rtype: None
    @rtype: int
   """

   if (n < 0):
       return None
   else:
       sum = 1000
       for i in range(1, n + 1):
           sum += (1 / i ** 2)
   return sum

n = int(input("Enter a non-negative integer: "))
print(series_sum(n))

"""
QUESTION #3
"""
def pell(n):
    """
    Takes int n and returns nth Pell number. 
    If n is negative, returns None.
    @type n: int
    @rtype: None
    @rtype: int
    """
    if (n < 0):
        return None

    elif(n >= 0 and n <= 2):
        return int(n)

    else:
        return 2 * pell(n - 1) + pell(n - 2)

print(pell(16))
print(pell(-45))

"""
QUESTION #4
"""
def countMembers(s):
    """
    Takes string and returns # of characters defined as extrordinary.
    @type s: string
    @rtye: int
    """
    extraordinary = [chr(i) for i in range(ord('e'), ord('j') + 1)]
    extraordinary = extraordinary + [chr(i) for i in range(ord('F'), ord('X') + 1)]
    extraordinary = extraordinary + [str(i) for i in range(2, 7)]
    extraordinary = extraordinary + ['!', ',', '\\']
    
    counter = 0
     
    for chars in s:
        if chars in extraordinary:
            counter += 1
    
    return counter

print(countMembers("eb4h49jjd"))

"""
QUESTION #5
"""
def casual_number(s):
    """
    Returns number regardless of comma placement, letters.
    Precondition: commas are in meaningful places.
    @type s: string
    @rtype: string
    """
    str1 = ""
    empt1 = ""
    change = 0

    for i in range (0, len(s)):

        if (s[i] == ',') :
            str1 = str1
           
        elif (s[i].isdigit()):
            str1 = str1 + s[i]
            change = 1
           
        elif (s[i] == '-') :
            str1 = str1 + s[i]  
           
        else:
            return empt1
          
    if (change == 1):
        return str1
      
    else:
        return empt1

print(casual_number("7636882"))
print(casual_number("89, TTT, UUU, 33"))

"""
QUESTION #6
"""
def alienNumbers(s):
    """
    Returns integer value to decode alien communications.
    @type s: string
    @rtype: int
    """
    num = 0
    for i in s:
        if i is "T":
            num += 1024
        elif i is 'y':
            num += 598
        elif i is "!":
            num += 121
        elif i is "a":
            num += 42
        elif i is "N":
            num += 6
        elif i is "U":
            num += 1
    return num

print(alienNumbers("UUyN!"))
print(alienNumbers("!!"))

"""
QUESTION #7
"""
def alienNumbersAgain(s):
    """
    Returns integer value to decode alien communications without string methods.
    @type s: string
    @rtype: int
    """
    counter = 0
    num = 0
    i = 0

    for i in s:
        counter = counter + 1
    i = 0

    while (i < counter):
        num = num + alienNumbers(s[i])
        i += 1
    return num

print(alienNumbersAgain("a!ya!U!NaU"))
print(alienNumbersAgain(""))

"""
QUESTION #8
"""
def encrypt(s):
    """
    Decrypts a secret code.
    @type s: str
    @rtype: str
    """
    str1 = s[::-1] 
    str2 = ""

    for i in range(len(s) // 2):
        str2 = str2 + str1[i] + s[i]

        if (len(s)%2 != 0) and (i == (len(s)/2 - 1)) :
            str2 = str2 + str1[i+1]
          
    return str2

print(encrypt("uOttawa engineering"))
print(encrypt("This is a message"))

"""
QUESTION #9
"""
def weaveop(s):
    """
    Returns string based on specific parameters.
    @type s: str
    @rtype: str
    """
    
    str1 = ''

    for i in range(0, len(s) - 1):
        str1 += s[i]
        
        if s[i].isalpha() and s[i + 1].isalpha():
            if s[i].isupper():
                str1 += 'O'
            else:
                str1 += 'o'
        
        if s[i + 1].isalpha() and s[i].isalpha():
            if s[i + 1].isupper():
                str1 += 'P'
            else:
                str1 += 'p'
    
    str1 += s[-1]
    return str1

print(weaveop("6838373"))
print(weaveop("aGfboU22"))

"""
QUESTION #10
"""
def squarefree(s):
    """
    Returns bool based on if given string 
    is Squarefree (does not contain subword twice).
    @type s: string 
    @rtype: bool
    """
    for i in range(1, int(len(s)/2) + 1):
        for x in range(len(s)):
            if((x + 2 * i) <= len(s)):
                if((s[x:x + i]) == (s[x + i:x + 2 * i])):
                    return False

    return True

print(squarefree("repetition"))
print(squarefree("jhsksojb"))