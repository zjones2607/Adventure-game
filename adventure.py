"""
Text-Based Adventure Game
A fantasy RPG where players explore locations, battle monsters, collect treasure, and manage their health.

Classes:
    Player: Manages player attributes (name, health, inventory, score)
    
Functions:
    random_encounter(): Generates random game events (monsters, treasures, allies)
    explore_forest(): Forest location with unique events
    explore_cave(): Cave location with unique events
    explore_village(): Village location with unique events
    explore_castle(): Castle location with unique events
    display_status(): Shows player stats and inventory
    display_help(): Shows available commands
    main(): Main game loop
"""

import random
from typing import List, Dict


class Player:
    """
    Represents the player in the adventure game.
    
    Attributes:
        name (str): The player's name
        health (int): Current health points (0-100)
        max_health (int): Maximum health points
        inventory (List[str]): List of items the player is carrying
        score (int): Current score/experience points
        current_location (str): Current location in the game world
    """
    
    def __init__(self, name: str):
        """Initialize a new player with default stats."""
        self.name = name
        self.health = 100
        self.max_health = 100
        self.inventory = []
        self.score = 0
        self.current_location = "starting_area"
    
    def add_item(self, item: str) -> None:
        """Add an item to the player's inventory."""
        self.inventory.append(item)
        print(f"✓ Gained: {item}")
    
    def remove_item(self, item: str) -> bool:
        """Remove an item from inventory if it exists."""
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False
    
    def take_damage(self, damage: int) -> None:
        """Reduce health by damage amount."""
        self.health = max(0, self.health - damage)
        if self.health == 0:
            print(f"\n💀 {self.name} has been defeated!")
    
    def heal(self, amount: int) -> None:
        """Restore health up to max_health."""
        self.health = min(self.max_health, self.health + amount)
        print(f"✓ Healed {amount} HP! Current health: {self.health}/{self.max_health}")
    
    def add_score(self, points: int) -> None:
        """Award points to the player."""
        self.score += points
        print(f"✓ Gained {points} points! Total score: {self.score}")
    
    def is_alive(self) -> bool:
        """Check if player is still alive."""
        return self.health > 0


def random_encounter() -> Dict[str, any]:
    """
    Generate a random encounter for the player.
    
    Returns:
        Dictionary with encounter type and details:
        - 'type': 'monster', 'treasure', or 'ally'
        - 'name': Name of the encounter
        - 'damage' or 'reward': Relevant values
    """
    encounter_type = random.choice(['monster', 'treasure', 'ally'])
    
    encounters = {
        'monster': [
            {'name': 'Goblin', 'damage': 15},
            {'name': 'Orc Warrior', 'damage': 25},
            {'name': 'Troll', 'damage': 35},
            {'name': 'Shadow Beast', 'damage': 40},
        ],
        'treasure': [
            {'name': 'Gold Coins', 'reward': 50, 'item': 'Gold Coins'},
            {'name': 'Mystical Gem', 'reward': 100, 'item': 'Mystical Gem'},
            {'name': 'Ancient Map', 'reward': 75, 'item': 'Ancient Map'},
            {'name': 'Treasure Chest', 'reward': 150, 'item': 'Treasure Chest'},
        ],
        'ally': [
            {'name': 'Brave Knight', 'gift': 'Sword', 'reward': 30},
            {'name': 'Wise Sage', 'gift': 'Healing Potion', 'reward': 40},
            {'name': 'Ranger', 'gift': 'Arrow Bundle', 'reward': 25},
        ]
    }
    
    return random.choice(encounters[encounter_type]), encounter_type


def explore_forest(player: Player) -> None:
    """
    Explore the Dark Forest location.
    Random encounter with consequences based on player actions.
    """
    print("\n" + "="*50)
    print("🌲 You walk into a dark, misty forest...")
    print("="*50)
    
    encounter, encounter_type = random_encounter()
    
    if encounter_type == 'monster':
        print(f"A wild {encounter['name']} appears!")
        action = input("Do you [fight], [run], or [negotiate]? ").lower()
        
        if action == 'fight':
            print(f"⚔️  You bravely fight the {encounter['name']}!")
            damage_taken = random.randint(5, encounter['damage'])
            player.take_damage(damage_taken)
            player.add_item(f"Tattered Fur from {encounter['name']}")
            player.add_score(50)
            print(f"You took {damage_taken} damage but won the battle!")
        elif action == 'run':
            print("💨 You escape safely, but miss out on potential treasure.")
            player.add_score(10)
        elif action == 'negotiate':
            if random.random() > 0.5:
                print("The creature agrees to let you pass safely.")
                player.add_score(20)
            else:
                print("The creature is not interested in negotiating!")
                player.take_damage(10)
        else:
            print("You hesitate in confusion... the creature attacks!")
            player.take_damage(20)
    
    elif encounter_type == 'treasure':
        print(f"You discover a {encounter['name']}!")
        player.add_item(encounter['item'])
        player.add_score(encounter['reward'])
    
    elif encounter_type == 'ally':
        print(f"You meet a {encounter['name']}!")
        player.add_item(encounter['gift'])
        player.add_score(encounter['reward'])


def explore_cave(player: Player) -> None:
    """
    Explore the Dark Cave location.
    Typically contains tougher monsters and better rewards.
    """
    print("\n" + "="*50)
    print("⛰️  You enter a dark cave. Your torch illuminates ancient stones...")
    print("="*50)
    
    encounter, encounter_type = random_encounter()
    
    if encounter_type == 'monster':
        print(f"A {encounter['name']} emerges from the shadows!")
        action = input("Do you [fight], [run], or [sneak]? ").lower()
        
        if action == 'fight':
            print(f"⚔️  Intense battle with {encounter['name']}!")
            damage_taken = random.randint(10, encounter['damage'])
            player.take_damage(damage_taken)
            player.add_item(f"Fang of {encounter['name']}")
            player.add_score(75)
            print(f"You took {damage_taken} damage but won!")
        elif action == 'run':
            print("You sprint back out of the cave!")
            player.add_score(15)
        elif action == 'sneak':
            if random.random() > 0.6:
                print("You sneak past the monster unnoticed!")
                player.add_score(35)
            else:
                print("You step on loose rocks and alert the monster!")
                player.take_damage(25)
        else:
            print("You panic! The monster attacks!")
            player.take_damage(30)
    else:
        print(f"You discover: {encounter['name']}!")
        if encounter_type == 'treasure':
            player.add_item(encounter['item'])
            player.add_score(encounter['reward'] + 25)
        else:
            player.add_item(encounter['gift'])
            player.add_score(encounter['reward'] + 15)


def explore_village(player: Player) -> None:
    """
    Explore the Peaceful Village location.
    Merchant quests and peaceful encounters.
    """
    print("\n" + "="*50)
    print("🏘️  You arrive at a peaceful village with warm lights in windows...")
    print("="*50)
    
    action = input("Do you [visit tavern], [trade with merchant], or [help villager]? ").lower()
    
    if action == 'visit tavern':
        print("You enjoy warm ale and hear tales of adventure.")
        if random.random() > 0.5:
            print("A patron gifts you a map!")
            player.add_item("Worn Map")
            player.add_score(30)
        else:
            print("You rest and recover.")
            player.heal(30)
    elif action == 'trade with merchant':
        print("The merchant offers rare items for sale.")
        if "Gold Coins" in player.inventory:
            print("You trade your Gold Coins for a Legendary Scroll!")
            player.remove_item("Gold Coins")
            player.add_item("Legendary Scroll")
            player.add_score(40)
        else:
            print("You don't have items the merchant wants.")
    elif action == 'help villager':
        print("An elderly villager thanks you for your kindness.")
        player.heal(20)
        player.add_score(50)
    else:
        print("You wander around the village aimlessly.")


def explore_castle(player: Player) -> None:
    """
    Explore the Mystical Castle location.
    Boss-level encounter with high stakes.
    """
    print("\n" + "="*50)
    print("👑 You stand before a magnificent, ancient castle...")
    print("="*50)
    
    encounter, encounter_type = random_encounter()
    
    if encounter_type == 'monster':
        print(f"A powerful {encounter['name']} guards the castle!")
        action = input("Do you [challenge], [retreat], or [use magic]? ").lower()
        
        if action == 'challenge':
            print(f"⚔️  BOSS BATTLE: {encounter['name']}!")
            if random.random() > 0.4:
                print("You defeat the boss! The castle is yours!")
                player.add_item("Crown of Kings")
                player.add_item("Royal Scepter")
                player.add_score(200)
            else:
                print("The boss is too powerful!")
                player.take_damage(50)
        elif action == 'retreat':
            print("You wisely retreat from this challenge.")
            player.add_score(20)
        elif action == 'use magic':
            if "Mystical Gem" in player.inventory or "Legendary Scroll" in player.inventory:
                print("Your magic overwhelms the guardian!")
                player.add_score(150)
            else:
                print("You lack the magical knowledge!")
                player.take_damage(35)
        else:
            print("You stand frozen in awe. The guardian attacks!")
            player.take_damage(45)
    else:
        print(f"You discover: {encounter['name']}!")
        if encounter_type == 'treasure':
            player.add_item(encounter['item'])
            player.add_score(encounter['reward'] + 50)
        else:
            player.add_item(encounter['gift'])
            player.add_score(encounter['reward'] + 25)


def display_status(player: Player) -> None:
    """Display player's current stats and inventory."""
    print("\n" + "="*50)
    print(f"📊 STATUS - {player.name}")
    print("="*50)
    print(f"Health:    {player.health}/{player.max_health} ", end="")
    
    # Health bar
    health_bar = "█" * (player.health // 10) + "░" * (10 - player.health // 10)
    print(f"[{health_bar}]")
    print(f"Score:     {player.score} XP")
    print(f"Location:  {player.current_location}")
    print(f"\nInventory ({len(player.inventory)} items):")
    
    if player.inventory:
        for i, item in enumerate(player.inventory, 1):
            print(f"  {i}. {item}")
    else:
        print("  (empty)")
    print("="*50)


def display_help() -> None:
    """Display available game commands."""
    print("\n" + "="*50)
    print("📖 AVAILABLE COMMANDS")
    print("="*50)
    print("  explore   - Go to a location to adventure")
    print("  status    - View your health, inventory, and score")
    print("  inventory - List all items in your inventory")
    print("  heal      - Use a Healing Potion if you have one")
    print("  help      - Show this menu")
    print("  quit      - Exit the game")
    print("="*50)


def main():
    """Main game loop. Handles user input and game flow."""
    print("\n" + "="*50)
    print("⚔️  WELCOME TO THE ADVENTURE GAME ⚔️")
    print("="*50)
    player_name = input("Enter your name, adventurer: ").strip() or "Adventurer"
    player = Player(player_name)
    print(f"\nWelcome, {player.name}! Your journey begins...\n")
    
    display_help()
    
    # Main game loop
    while player.is_alive():
        try:
            command = input(f"\n[{player.name}] > ").lower().strip()
            
            if command == "explore":
                location = input("Where would you like to go? [forest/cave/village/castle]: ").lower()
                if location == "forest":
                    player.current_location = "Dark Forest"
                    explore_forest(player)
                elif location == "cave":
                    player.current_location = "Dark Cave"
                    explore_cave(player)
                elif location == "village":
                    player.current_location = "Peaceful Village"
                    explore_village(player)
                elif location == "castle":
                    player.current_location = "Mystical Castle"
                    explore_castle(player)
                else:
                    print("Unknown location. Try: forest, cave, village, or castle")
            
            elif command == "status":
                display_status(player)
            
            elif command == "inventory":
                print(f"\n📦 {player.name}'s Inventory ({len(player.inventory)} items):")
                if player.inventory:
                    for item in player.inventory:
                        print(f"  • {item}")
                else:
                    print("  (empty)")
            
            elif command == "heal":
                if "Healing Potion" in player.inventory:
                    player.remove_item("Healing Potion")
                    player.heal(50)
                else:
                    print("You don't have a Healing Potion!")
            
            elif command == "help":
                display_help()
            
            elif command == "quit":
                print(f"\n👋 Thanks for playing, {player.name}!")
                print(f"Final Score: {player.score} XP")
                print("Goodbye!\n")
                break
            
            else:
                print("Unknown command. Type 'help' for available commands.")
            
        except KeyboardInterrupt:
            print(f"\n\n👋 Thanks for playing, {player.name}! See you next time!")
            break
        except Exception as e:
            print(f"An error occurred: {e}. Try again.")


if __name__ == "__main__":
    main()