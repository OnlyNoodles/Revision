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
                          "To exit, enter 'X'.\nType here: ").upper()
    if building_type == "X":
        break
    elif building_type != "C" and building_type != "R":
        print("Please enter a valid building type.")
    else:
        length = number_checker("Enter the length (metres) of the foundation slab: ")
        width = number_checker("Enter the width (metres) of the foundation slab: ")

        area = length * width
        if building_type == "C":
            volume = area * depth_commercial
        elif building_type == "R":
            volume = area * depth_residential

        print(f"Area: {area} square metres")
        print(f"Volume: {volume} cubic metres")
