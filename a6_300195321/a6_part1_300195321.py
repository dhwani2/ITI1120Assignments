import string

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    while True:
        
        try:
            enterFile = input("Enter file name: ")
            file = open(enterFile, "r")
            return file
        
        except:
            print("No such file exists, try again: ")

def no_punctuation(word):
    allowed = "abcdefghijklmnopqrstuvwxyz"
    newOne = ""
    
    for i in word:
        if i in allowed:
            newOne += i
    
    return newOne


def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    D = {}
    list1 = []
    
    for list2 in fp:
        list2_new = list2.lower()
        list2_new = list2_new.strip()
        list2_new = list2_new.split(" ")
        for i in range(len(list2_new)):
            string = list2_new[i]
            string = list(string)
            string = no_punctuation(string)
            string = "".join(string)
            string = string.strip()
            if (len(string) >= 2):
                list2_new[i] = string
        list1.append(list2_new)
    
    for list2_no in range(len(list1)):
        for word in list1[list2_no]:
            if (word not in D.keys()):
                D[word] = {list2_no+1}
            else:
                D[word].add(list2_no+1)
    
    return D

def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    query = [x.strip() for x in query.split(" ")]
    if query[0] in D.keys():
        S = D[query[0]]
    else:
        print("Word '{}' not found in the file".format(query[0]))
        return -1
    for index in range(1, len(query)):
        if query[index] in D.keys():
            S_new = D[query[index]]
            S = S.intersection(S_new)
        else:
            print("Word '{}' not found in the file".format(query[index]))
            return -1
    S = list(S)
    S.sort()
    return S
    

##############################
# main
##############################

# YOUR CODE GOES HERE
while True:
    file = open_file()
    D = read_file(file)
    query = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
    if query == 'q':
        break
    A = find_coexistance(D, query)
    if A == -1:
        continue
    elif len(A) == 0:
        print("Entered words do not exist in the same line of the file")
    else:
        print("Entered words exist in the same line of the file")
        print(" ".join([str(x) for x in A]))
