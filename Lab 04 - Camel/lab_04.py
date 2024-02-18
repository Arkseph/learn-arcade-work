import random
def menu():
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")

def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_distance = -20
    canteen_drinks = 3

    # The natives are 10 miles behind you.

    done = False
    while not done:
        menu()
        user_choice = input("What is your choice? ").upper()

        if user_choice == 'Q':
            print("You quit the game.")
            break

        elif user_choice == 'B':  # Ahead moderate speed
            thirst += 1
            miles = random.randrange(5, 12)
            miles_traveled += miles
            camel_tiredness += 1
            natives_distance += random.randrange(7, 14)
            print("You traveled", miles, "miles.")

        elif user_choice == 'C':  # Ahead full speed
            thirst += 1
            miles = random.randrange(10, 21)
            miles_traveled += miles
            camel_tiredness += random.randrange(1, 3)
            natives_distance += random.randrange(7, 14)
            print("You traveled", miles, "miles.")

        elif user_choice == 'D':  # Stop for the night
            camel_tiredness = 0
            print("The camel is happy and rested now.")
            natives_distance += random.randrange(7, 14)

        elif user_choice == 'E':  # Status
            print("Miles traveled:", miles_traveled)
            print("Drinks in canteen:", canteen_drinks)
            print("The natives are", miles_traveled - natives_distance, "miles behind you.")

        elif user_choice == 'A':  # Drink
            if canteen_drinks > 0:
               canteen_drinks -= 1
               thirst = 0
               print("You drank from your canteen.")
            else:
               print("Your canteen is empty.")

        else:                          # Error
            print("Invalid choice.")

        if not done and 4 < thirst <= 6:                  # Thirst
            print("You are thirsty.")
        elif thirst > 6:
            print("You died of thirst!")
            done = True

        if not done and 5 < camel_tiredness >= 8:             # Camel tiredness
            print("Your camel is getting tired.")
        elif not done and camel_tiredness > 8:
            print("Your camel is dead.")
            done = True

        if natives_distance >= miles_traveled:     # Natives
            print("The natives caught you!")
            done = True
        elif natives_distance >= miles_traveled - 15:
            print("The natives are getting close! ")

        elif miles_traveled >= 200:      # Win
            print("Congratulations! You won the game and a camel!")
            done = True

        if user_choice == 'B' and random.randrange(1, 21) == 7:  # Oasis
            drinks_in_canteen = 3
            thirst = 0
            camel_tiredness = 0
            print("Nice, you found an oasis! Your canteen is refilled and your camel rested.")
        if user_choice == 'C' and random.randrange(1, 21) == 7:
            drinks_in_canteen = 3
            thirst = 0
            camel_tiredness = 0
            print("Nice, you found an oasis! Your canteen is refilled and your camel rested.")
main()