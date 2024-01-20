def isTriangularNumber(num):
    # method 1 using a loop
    # starting at 1 and calculates always the next triangular number
    # until the result is equal or larger than the number under test

    result = int(0)
    iterator = int(1)

    while result<num:
        result = result + iterator
        iterator += 1
    
    if result == num:
        return True
    else:
        return False
    
def bisection():
    # to be implemented
    print()

