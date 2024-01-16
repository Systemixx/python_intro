def adventure_game():
    location = "forest"
    while True:
        if location == "forest":
            print("You are in a forest. You can go north or east.")
            choice = input("Which way? ")
            if choice == "north":
                location = "river"
            elif choice == "east":
                location = "mountain"
            else:
                print("Invalid choice.")

        elif location == "river":
            print("You are by a river. You can go south or east.")
            choice = input("Which way? ")
            if choice == "south":
                location = "forest"
            elif choice == "east":
                location = "village"
            else:
                print("Invalid choice.")

        elif location == "mountain":
            print("You are on a mountain. You can go west.")
            choice = input("Which way? ")
            if choice == "west":
                location = "forest"
            else:
                print("Invalid choice.")

        elif location == "village":
            print("You reached a village! You win!")
            break

adventure_game()
