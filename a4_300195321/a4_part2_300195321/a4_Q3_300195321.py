
def longest_run(nums):
    """
    Returns longest run given an int list
    @type nums: list
    @rtype: int 
    """
    maxCount = 0
    counter = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            if counter > maxCount:
                maxCount = counter
            counter = 1
        else:
            counter += 1
    
    if (len(nums) > 0 and counter > maxCount):
        maxCount = counter
    
    return maxCount

nums = []
numList = input("Please input a list of numbers separated by space: ").strip().split()


for i in numList:
  if (i.strip() != ""):
    nums.append(float(i))

print(longest_run(nums))