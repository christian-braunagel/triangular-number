import triangular_math

exit = bool(False)

while(not exit):

    # ask for user input
    triangular_num = input("Which triangular number should be visualized? Type 'q' to quit.\n")

    # user wants to exit
    if triangular_num == 'q':
        exit = True
        continue

    # basic checks for input
    try:
        tested_num = int(triangular_num)
        if tested_num < 1:
            print("Your input is not a positive integer.")
    except ValueError:
        print("Your input is not a integer.")

    # check if it is a triangular number
    # if not triangular_math.isTriangularNumber(triangular_num):
    #     print('Your input is not a triangular number.')
    #     continue

