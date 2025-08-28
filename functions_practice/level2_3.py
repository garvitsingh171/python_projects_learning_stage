# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a,b,c):
    sum = a+b+c
    if sum <= 21:
        return sum
    elif sum > 21:
        if a==11 or b==11 or c==11:
            return sum-10
        else:
            return "BUST"
    else:
        return "BUST"
print(blackjack(3,12,70))