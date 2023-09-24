# Define an enum for item types
from enum import Enum

class ItemType(Enum):
    WEAPON = "weapon"
    ARMOR = "armor"
    ITEM = "item"

# Define a class to represent items in the game with a type classification
class GameItem:
    """Represents an item in the game."""
    
    def __init__(self, id, name, item_type, quantity):
        """
        Initialize a GameItem.

        Args:
            id (int): The unique identifier for the item.
            name (str): The name of the item.
            item_type (ItemType): The type of the item (weapon, armor, or item).
            quantity (int): The quantity of the item.
        """
        self.id = id
        self.name = name
        self.item_type = item_type
        self.quantity = quantity

# Create a class to manage the player's inventory
class PlayerInventory:
    """Manages the player's inventory."""
    
    def __init__(self, max_capacity):
        """
        Initialize a PlayerInventory.

        Args:
            max_capacity (int): The maximum capacity of the inventory.
        """
        self.max_capacity = max_capacity
        # Use dictionaries to store game items in separate compartments
        self.weapons = {}
        self.armor = {}
        self.items = {}

    def add_item(self, item):
        """
        Add a new item to the inventory and assign it to the correct compartment based on its type.

        Args:
            item (GameItem): The item to be added.
        """
        if self.is_inventory_full():
            print(f"Inventory is full. Cannot add {item.name}.")
            return

        compartment = None
        if item.item_type == ItemType.WEAPON:
            compartment = self.weapons
        elif item.item_type == ItemType.ARMOR:
            compartment = self.armor
        elif item.item_type == ItemType.ITEM:
            compartment = self.items

        if compartment is not None:
            if item.id in compartment:
                compartment[item.id].quantity += item.quantity
            else:
                compartment[item.id] = item
        else:
            print("Invalid item type.")

    def remove_item_by_id(self, item_id):
        """
        Remove an item from the inventory by ID.

        Args:
            item_id (int): The ID of the item to be removed.
        """
        for compartment in [self.weapons, self.armor, self.items]:
            if item_id in compartment:
                del compartment[item_id]
                return

    def update_item_quantity(self, item_id, new_quantity):
        """
        Update the quantity of an item in the inventory.

        Args:
            item_id (int): The ID of the item to be updated.
            new_quantity (int): The new quantity of the item.
        """
        for compartment in [self.weapons, self.armor, self.items]:
            if item_id in compartment:
                compartment[item_id].quantity = new_quantity
                return

    def list_items_in_compartment(self, compartment_name):
        """
        List all items in a specific compartment.

        Args:
            compartment_name (str): The name of the compartment (weapons, armor, or items).
        """
        print(f"{compartment_name.capitalize()}:")
        compartment = None
        if compartment_name == "weapons":
            compartment = self.weapons
        elif compartment_name == "armor":
            compartment = self.armor
        elif compartment_name == "items":
            compartment = self.items

        if compartment is not None:
            for item in compartment.values():
                print(f"{item.name} (ID: {item.id}) - Quantity: {item.quantity}")
        else:
            print("Invalid compartment.")

    def is_inventory_full(self):
        """
        Check if the inventory is full.

        Returns:
            bool: True if the inventory is full, False otherwise.
        """
        total_items = len(self.weapons) + len(self.armor) + len(self.items)
        return total_items >= self.max_capacity

# Example usage
if __name__ == "__main__":
    # Create an instance of the PlayerInventory class with a maximum capacity of 10
    player_inventory = PlayerInventory(10)

    # Add some items to the player's inventory with automatic type detection
    player_inventory.add_item(GameItem(1, "Sword", ItemType.WEAPON, 1))
    player_inventory.add_item(GameItem(2, "Shield", ItemType.ARMOR, 1))
    player_inventory.add_item(GameItem(3, "Health Potion", ItemType.ITEM, 5))
    player_inventory.add_item(GameItem(4, "Bow", ItemType.WEAPON, 1))

    # List all items in each compartment
    player_inventory.list_items_in_compartment("weapons")
    player_inventory.list_items_in_compartment("armor")
    player_inventory.list_items_in_compartment("items")

    # Remove an item from the player's inventory
    player_inventory.remove_item_by_id(2)

    # List items in the armor compartment after removal
    player_inventory.list_items_in_compartment("armor")

    # Update the quantity of an item
    player_inventory.update_item_quantity(1, 2)

    # List items in the weapons compartment after updating quantity
    player_inventory.list_items_in_compartment("weapons")
