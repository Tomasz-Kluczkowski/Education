from unit_testing import test

def add_fruit(inventory: dict, fruit, quantity=0):
    """Adds quantity of fruit to the inventory"""

    inventory[fruit] = inventory.get(fruit, 0) + quantity




new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
test("strawberries" in new_inventory, True)
test(new_inventory["strawberries"], 10)
add_fruit(new_inventory, "strawberries", 25)
test(new_inventory["strawberries"], 35)