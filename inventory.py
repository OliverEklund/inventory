from abc import ABC, abstractmethod
from typing import List

class Item:
    def __init__(self, name, spaces = 0, uses = 0):
        self.name = name
    @abstractmethod
    def use(self):
        print("Du använder" + self.name)

class Lead_pipe(Item):
    def use(self):
        print("Clang!")

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
            self.contents.remove(item)
        else:
            pass

player_inventory = Inventory()
hagelbössa = Item("Hagelbössa", 7, 2)
wienerbröd = Item("Stort Wienerbröd", 1, 5)
Sten = Item("Sten", 2, 1)
player_inventory.add_item(hagelbössa)
player_inventory.add_item(Sten)
player_inventory.add_item(wienerbröd)

for item in player_inventory.get_contents():
    print(item.name)

input("")
player_inventory.remove_item(hagelbössa)

for item in player_inventory.get_contents():
    print(item.name)
