
def two_length_run(list):
    """
    Returns true or false
    @type list: list
    @rtype ans: bool
    """
    i = 0
    list = input("Enter a list of numbers with commas: ")
    if (len(list) <= 1):
        return False

    else:
        list = [int(inputnumber) for inputnumber in list.split(',')]
        for i in range(0, len(list) - 1):
            if list[i] == list[i+1]:
                ans = True
                return ans
            else:
                ans = False
        return ans

print(two_length_run(list))