# FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(list):
    for num in range(0,len(list)-1):
        if list[num:num+2] == [3,3]:
            return True
    return None
print(has_33([6,8,9,3,5,3,4]))
