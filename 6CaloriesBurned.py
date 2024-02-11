def workout():
    bicycling = float(input("Enter the amount of hours you spent bicycling: "))
    jogging = float(input("Enter the amount of hours spent jogging: "))
    swimming = float(input("Enter the amount of hours you spent swimming: "))
    calories = (bicycling * 200 + jogging * 475 + swimming * 275)
    kilograms = calories / 3500 * 454 / 1000
    print(f"You have lost {kilograms: .2f} kilograms.")


if __name__ == "__main__":
    workout()
