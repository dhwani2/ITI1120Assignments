
def number_divisible(list1, num):
    """
    Returns  number of elements in the list divisible by n
    @type list1: int list
    @type num: int
    @rtype counter: int
    """
    counter = 0
    for i in list1:
        if(i % num == 0):
            counter += 1
    return counter


s = input("Please input a list of integers separated by spaces: ")
list1 = [int(i) for i in s.split(" ")]

num = int(input("Please input an integer: "))
print(number_divisible(list1, num))