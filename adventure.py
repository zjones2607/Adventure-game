import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.score = 0
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(f"> You obtained: {item}")

    def take_damage(self, amount):
        self.health -= amount
        print(f"> You took {amount} damage! Health is now {self.health}.")

    def add_score(self, points):
        self.score += points
        print(f"> You gained {points} points! Score: {self.score}")

    def show_status(self):
        print("\n===== STATUS =====")
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Score: {self.score}")
        print(f"Inventory: {self.inventory if self.inventory else 'Empty'}")
        print("==================\n")

    def show_inventory(self):
        print("\n===== INVENTORY =====")
        if not self.inventory:
            print("You are carrying nothing.")
        else:
            for index, item in enumerate(self.inventory, 1):
                print(f"{index}. {item}")
        print("=====================\n")

    def use_item(self, item_name):
        if item_name not in self.inventory:
            print(f"> You don't have a {item_name}.")
            return

        # Healing Items
        if item_name in ["Healing Potion", "Healing Herb"]:
            heal_amount = 30 if item_name == "Healing Potion" else 15
            self.health = min(100, self.health + heal_amount)
            print(f"> You used {item_name} and recovered {heal_amount} health!")
            self.inventory.remove(item_name)
        else:
            print(f"> You can't use {item_name} right now.")

    def heal(self):
        # Auto-use the best healing item if available
        healing_items = ["Healing Potion", "Healing Herb"]

        for item in healing_items:
            if item in self.inventory:
                self.use_item(item)
                return

        print("> You have no healing items!")


def random_encounter(player):
    encounters = ["monster", "treasure", "ally"]
    event = random.choice(encounters)

    if event == "monster":
        print("A wild monster jumps out!")
        action = input("Do you [fight] or [run]? ")

        if action.lower() == "fight":
            print("You fight bravely...")
            if random.random() < 0.7:
                print("You defeated the monster!")
                player.add_score(20)
                if random.random() < 0.5:
                    player.add_item("Monster Fang")
            else:
                print("You won, but got injured!")
                player.take_damage(20)
                player.add_score(10)

        elif action.lower() == "run":
            print("You escaped, but dropped some gold!")
            player.add_score(-5)

        else:
            print("You hesitate and the creature bites you before vanishing!")
            player.take_damage(15)

    elif event == "treasure":
        loot = random.choice(["Gold Coin", "Healing Potion", "Ancient Relic"])
        print(f"You found a treasure chest with a {loot}!")
        player.add_item(loot)
        player.add_score(15)

    elif event == "ally":
        print("A friendly traveler gives you supplies.")
        player.add_item("Healing Herb")
        player.add_score(10)


def explore(player):
    print("You walk deeper into the wilderness...")
    random_encounter(player)


def visit_cave(player):
    print("\nYou enter a damp, echoing cave...")
    if random.random() < 0.6:
        random_encounter(player)
    else:
        print("It's quiet... too quiet. You find nothing.")


def visit_village(player):
    print("\nYou arrive at a small village.")
    print("A merchant offers you a Healing Potion for 10 points.")
    buy = input("Buy it? [yes/no] ")

    if buy.lower() == "yes" and player.score >= 10:
        player.score -= 10
        player.add_item("Healing Potion")
    elif buy.lower() == "yes":
        print("You don’t have enough points!")
    else:
        print("You leave the merchant.")


def visit_castle(player):
    print("\nYou approach a mysterious old castle...")
    event = random.choice(["battle", "treasure", "nothing"])

    if event == "battle":
        print("A knight challenges you!")
        player.take_damage(25)
        player.add_score(30)

    elif event == "treasure":
        print("You discover the royal vault!")
        player.add_item("Jeweled Crown")
        player.add_score(50)

    else:
        print("The castle halls are empty and cold.")


def show_help():
    print("\n===== HELP MENU =====")
    print("explore    - Explore the wilderness")
    print("cave       - Enter the cave")
    print("village    - Visit the village shop")
    print("castle     - Explore the castle")
    print("status     - Show health, score, inventory")
    print("inventory  - Show your inventory")
    print("heal       - Automatically use a healing item")
    print("use <item> - Use a specific item (e.g. 'use Healing Potion')")
    print("help       - Show all commands")
    print("quit       - Exit the game")
    print("======================\n")


def main():
    name = input("Enter your name, adventurer: ")
    player = Player(name)
    print(f"Welcome, {player.name}! Your journey begins...\n")

    print("Type 'help' to see all commands.")

    while True:
        command = input("> ").lower()

        if command == "explore":
            explore(player)

        elif command == "cave":
            visit_cave(player)

        elif command == "village":
            visit_village(player)

        elif command == "castle":
            visit_castle(player)

        elif command == "status":
            player.show_status()

        elif command == "inventory":
            player.show_inventory()

        elif command == "heal":
            player.heal()

        elif command.startswith("use "):
            item_name = command[4:].strip().title()
            player.use_item(item_name)

        elif command == "help":
            show_help()

        elif command == "quit":
            print("Thanks for playing!")
            break

        else:
            print("Unknown command. Type 'help' for a full list.")


if __name__ == "__main__":
    main()
