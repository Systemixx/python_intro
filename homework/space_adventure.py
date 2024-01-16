def space_adventure_game():
    current_location = "Central Hub"
    inventory = []

    locations = {
        "Central Hub": {
            "description": "You are in the central hub of a space station. Paths lead to the living quarters, the engine room, and the control room.",
            "east": "Living Quarters",
            "west": "Engine Room",
            "north": "Control Room",
            "item": "flashlight"
        },
        "Living Quarters": {
            "description": "You are in the living quarters. You can go back to the central hub or explore the lab.",
            "west": "Central Hub",
            "north": "Lab",
            "item": "food supplies"
        },
        "Engine Room": {
            "description": "You are in the engine room. You need a toolkit to fix the engine.",
            "east": "Central Hub",
            "challenge": "fix",
            "required_item": "toolkit"
        },
        "Control Room": {
            "description": "You are in the control room. From here, you can communicate with Earth.",
            "south": "Central Hub",
            "item": "communication logs"
        },
        "Lab": {
            "description": "You are in the lab. There's a toolkit here.",
            "south": "Living Quarters",
            "item": "toolkit"
        }
    }

    def get_item(location):
        item = locations[location].get("item")
        if item and item not in inventory:
            inventory.append(item)
            print(f"You found {item}!")

    def check_challenge(location):
        challenge = locations[location].get("challenge")
        required_item = locations[location].get("required_item")

        if challenge and required_item not in inventory:
            print(f"You need a {required_item} to {challenge} the engine.")
            return False
        return True

    while True:
        print(locations[current_location]["description"])
        get_item(current_location)

        command = input("What do you do? ").strip().lower()

        if command in ["north", "south", "east", "west"]:
            next_location = locations[current_location].get(command)
            if next_location:
                if check_challenge(next_location):
                    current_location = next_location
                    if current_location == "Engine Room" and "toolkit" in inventory:
                        print("You have fixed the engine and saved the space station! Congratulations, you win!")
                        break
            else:
                print("You can't go that way.")
        elif command == "inventory":
            print(f"Inventory: {', '.join(inventory)}")
        elif command == "quit":
            print("You have left the game.")
            break
        else:
            print("Invalid command. Try 'north', 'south', 'east', 'west', 'inventory', or 'quit'.")

space_adventure_game()
