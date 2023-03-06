# Family name: Dhwani Vaishnav
# Student number: 300195321
# Course: IT1 1120 
# Assignment Number 1
# year 2020

########################
# Question 1
########################

# create the poem generator function
def poem_generator():
  # ask user for name
   name = input("Enter your name: ")
   # ask user for city
   city = input("Enter your city: ")
   # print the poem
   # poem retrieved from HW1- ITI 1120-C
   print(name + " had funny hair\n"
   "With tons and tons to spare\n" +
   name + "'s hair clippings made a wig\n"
   "It was very big\nAnd caused the townsfolk" +
   " of " + city + " to stare")

# call the function
poem_generator()

#######################
# Question 2
#######################

# create the impl2loz function that takes w
def impl2loz(w):
  # resul
  result = w * 16
  # divide result by 3
  l = result // 3
  # subtract 1 from result
  o = result - l
  # return pair of solutions
  return(l, o)

# print two examples
print(impl2loz(2))
print(impl2loz(1))

#######################
# Question 3
#######################

# create the pale function
def pale(n):
    # calculate last 2 digits
    n1 = n % 100
    # calculate middle two digits
    n2 = (n // 10) % 100
    # calculate first two digits
    n3 = n // 100
    # calculate last digit
    lastDigit = n % 10
    # if n is not pale return false
    if ((n1 == 33 or n2 == 33 or n3 == 33) or (lastDigit%4 == 0)):
        return False
    # else if n is pale return true
    else:
        return True

# user to enter an n int
n = int(input("Enter a n: "))
# print and call the function
print(pale(n))

#######################
# Question 4
#######################

# create the bibformat function
def bibformat(author, title, city, publisher, year):
    # string format
    string = author +' (' + year +').' +" " + title +". "+ city  + ": " + publisher + "."
    return string

# print and call the bibformat function
print(bibformat("author", "title", "city", "publisher", "year"))

#######################
# Question 5
#######################


# create the bibformat function
def bibformat(author, title, city, publisher, year):
    # string format
    string = author +' (' + year +').' +" " + title +". "+ city  + ": " + publisher + "."
    return string

# print and call the bibformat function
print(bibformat("author", "title", "city", "publisher", "year"))

# create the bibformat_display function
def bibformat_display():

    # ask for author input
    author = input("Enter author: ")

    # ask for title input
    title = input("Enter title: ")

    # ask for city input
    city = input("Enter city: ")

    # ask for publisher input
    publisher = input("Enter publisher: ")

    # ask for year input
    year = input("Enter year: ")

    # print and call the bibformat function
    print(bibformat(author,title,city,publisher,year)) 
    
#call the bibformat_display function
bibformat_display()

#######################
# Question 6
#######################

# create the compound function
def compound(x, y, z):
  # return true or False
  # first for even numbers, next for pairs > 100
  return (x %2 == 0 and y %2 == 0 and z %2 == 0) and (x + y > 100 or y + z > 100 or x + z > 100)

#######################
# Question 7
#######################

# import math
import math

# create function funct
def funct(p):
  # ask user to enter a number >= 11
  p = int(input("Enter a number >= 11: "))
  # calculations format
  r = math.log10(p) / math.log10(5) ** (0.5)
  # print the solution and typecast r 
  print("The solution is " + str(r))

funct(10)

#######################
# Question 8
#######################

# import math
import math

# define the function gol
def gol(n):
  # use math functions (ceil, log) and perform
  # necessary operations
   return math.ceil(math.log(n, 2))

# print and call the function
print(gol(6.4))

#######################
# Question 9
#######################

# import math
import math

# define the cad_cashier(price, payment) function
def cad_cashier(price, payment):
  # enter input
  price = int(input("Enter first number: "))
  payment = int(input("Enter second number: "))
  # calculate price
  price = round(price / 5, 2)*5
  # return the price
  return round(payment - price, 2)

# print and call the function
print(cad_cashier(10, 11))

#######################
# Question 10
#######################

# create and call the function
def min_CAD_coins(price, payment):
  # variables and make an array
  toonies = 200
  loonies = 100
  quarters = 25
  dimes = 10
  nickels = 5
  result = []
  
  # difference for price and payment
  diff = cad_cashier(price, payment)
  # add to the array
  result.append(diff / toonies)

  diff = diff % toonies
  # add to the array
  result.append(diff / loonies)
  
  diff = diff % loonies
  # add to the array
  result.append(diff / quarters)

  diff = diff % quarters
  # add to the array
  result.append(diff / dimes)

  diff = diff % dimes
  # add to the array
  result.append(diff / nickels)

  # return the result
  return result

