import math_lib

def isTriangularNumberIterationMethod(num):
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

# function to determine the triangular number
def funcTriangularNum(x, constant):
    return x*x + x - constant

def isTriangularNumberZeroPoints(num):

    if num == 1 or num == 3:
        return True

    print(math_lib.hasSignChange(funcTriangularNum,-num, num))

def isTriangularNumberLookUpTable(num):
    print('implement a method to check triangular number with look up table')

