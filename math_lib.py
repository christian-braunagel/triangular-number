# create bisection

# check if function has a sign change between the start and end point
def hasSignChange(f, start, end):
    return f(start)*f(end) < 0