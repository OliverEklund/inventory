from abc import ABC, abstractmethod
from typing import List

class Item:
    def __init__(self, name, spaces = 0, uses = 0):
        self.name = name
        self.spaces = spaces
        self.uses = uses
    
    def use(self, inventory):
        print("Du använder " + self.name)
        self.uses -= 1
        if self.uses == 0:
            print(self.name + " kan inte användas något mer")
            inventory.remove_item(self)

class gun(Item):
    def use(self):
        print("bang!")

class Inventory():
    def __init__(self):
        self.contents = []
        spaces = 20
    
    def get_contents(self):
        return self.contents
    
    def add_item(self, item):
        self.contents.append(item)
    
    def remove_item(self, item):
        if item in self.contents:
            print(f"{item.name} removed from inventory")
            self.contents.remove(item)
        else:
            pass

player_inventory = Inventory()
hagelbössa = Item("Hagelbössa", 7, 2)
wienerbröd = Item("Stort Wienerbröd", 1, 5)
sten = Item("Sten", 2, 1)
player_inventory.add_item(hagelbössa)
player_inventory.add_item(sten)
player_inventory.add_item(wienerbröd)
hagelbössa.use(player_inventory)
hagelbössa.use(player_inventory)

for item in player_inventory.get_contents():
    print(item.name)

# input("")
player_inventory.remove_item(sten)

for item in player_inventory.get_contents():
    print(item.name)
