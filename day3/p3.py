level1 = input("Welcome to the island. Where do you want to go, left or right? ")

if level1 == "right":
    print("Game over.")    
else:
    level2 = input("Do you want to swim or wait? ")
    if level2 == "swim":
        print("Game over.")
    else:
        level3 = input("Which door do you choose: red, green, or blue? ")
    if level3 == "red" or level3 == "blue":  # Corrected condition
        print("Game over.")
    else:
        print("You win!")
