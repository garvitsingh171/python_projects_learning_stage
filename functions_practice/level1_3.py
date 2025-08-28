# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    if n in range (0,101):
        if 100-n in range(0,10):
            return True
        else:
            return False
    elif n in range(101,201):
        if n-100 in range(0,10) and 200-n in range(0,10):
            return True
        else:
            return False
    elif n in range(201,301):
        if n-200 in range(0,10):
            return True
        else:
            return False
    else:
        return False
print(almost_there(92))