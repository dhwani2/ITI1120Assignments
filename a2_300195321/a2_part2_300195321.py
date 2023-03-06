
# Question 1
def min_enclosing_rectangle(r, x, y):
  if (r > 0 and x > 0 and y > 0):
    first = x - r
    second = y - r
    print ("(" + str(first) + ", " + str(second) + ")")
  else: 
    return None

# call the function with values
min_enclosing_rectangle(1, 1, 1)
min_enclosing_rectangle(4.5, 10, 2)
min_enclosing_rectangle(-1, 10, 2)
min_enclosing_rectangle(500, 1000, 2000)

# Question 2
def vote_percentage(votes):
    # make a substring
    substring = [votes[i:j] for i in range(len(votes)) for j in range(i + 1, len(votes) + 1)]

    # vars for voting
    voteYes = 0
    voteNo = 0
    voteTotal = 0

    # for loop 
    for i in substring:
        # which one they have voted add to count
        if (i.lower() == "yes"):
            voteYes = voteYes + 1
        elif (i.lower() == "no"):
            voteNo = voteNo + 1

    # get the total no of votes
    voteTotal = voteYes + voteNo

    # if the vote total is true than return the percent by division
    if (voteTotal):
        percent = voteYes/voteTotal
        return percent
    else:
        return 0

# call the function with values
print(vote_percentage("yes yes yes yes yes abstained yes yes yes yes"))
print(vote_percentage('yes,yes, no, yes, no, yes, abstained, yes, yes, no'))
print(vote_percentage('abstained no abstained yes no yes no yes yes yes no'))
print(vote_percentage('no yes no no no yes yes yes no'))

# Question 3
def vote():
    voteTotal = voteYes + voteNo

    if (voteTotal == voteYes):
        print("Proposal passes unanimously")
    elif ((voteYes/2) >= 2/3):
        print("Proposal passes with super majority")
    elif ((voteYes/total) >= 1/2):
        print("Proposal passes with simple majority")
    else: 
        print("Proposal fails")