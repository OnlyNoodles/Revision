def number_checker(question):
    error = "\nPlease enter a valid number.\n"
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(error)

depth_commercial = 0.5
depth_residential = 0.25
volume = 0.0

while True:
    building_type = input("Enter what type of building you want to make.\n"
                          "For commercial, enter 'C'.\n"
                          "For residential, enter 'R'.\n"
                          "To exit, enter 'X'.\n").upper()
    if building_type == "X":
        break
    else:
        while building_type != "C" or building_type != "R":
            input("Please enter a valid building type.\n")

length = int(input("Enter the length of the foundation slab: "))
width = int(input("Enter the width of the foundation slab: "))

