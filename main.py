# ask for user input
exit = bool(False)

while(not exit):

    # ask for user input
    triangular_num = input("Which triangular number should be visualized? Type 'q' to quit.\n")

    # user wants to exit
    if triangular_num == 'q':
        exit = True
        continue

    # basic checks for input
    if not triangular_num.isnumeric():
        print("Your input is not a positive number.")
        continue


