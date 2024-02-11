def storm():
    seconds = float(input("Enter the amount of seconds between the lightning and thunder: "))
    how_far_away = (seconds * 340)
    kilometres = how_far_away / 1000
    print(f"The storm is {kilometres: .2f} kilometres away.")


if __name__ == "__main__":
    storm()
