# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_of_69(numberlist):
    addition_of_nums = 0
    for num in numberlist:
        if [num] != [6]:
            addition_of_nums = addition_of_nums + num
            return addition_of_nums
        else:
            addition_of_nums = addition_of_nums + 0
            return addition_of_nums
        # return addition_of_nums
print(summer_of_69([3,4,5,6,7,8]))