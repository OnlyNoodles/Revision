pi = 3.14159

while True:
    radius_input = input("Enter the radius of the sphere.\n"
                         "To exit, enter 'X'.\nType here: ")
    if radius_input.upper() == 'X':
        break
    try:
        radius = float(radius_input)
        area = 4 * pi * radius * radius
        volume = (4/3) * pi * radius ** 3

        print(f"Area: {area:.2f} square centimetres")
        print(f"Volume: {volume:.2f} cubic centimetres")
    except ValueError:
        print("Please enter a valid number for the radius.")
