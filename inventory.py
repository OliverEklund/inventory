from abc import ABC, abstractmethod
from typing import List

class Item:
    def __init__(self, name):
        self.name = name
    def use(self):
        pass

class Lead_pipe(Item):
    def use(self):
        print("Clang!")

class Inventory():
    def __init__(self):
        self.contents = []
    
    def get_contents(self):
        return self.contents
    
    @abstractmethod
    def add_item(self, item):
        self.contents.append(item)

player_inventory = Inventory()
hagelbössa = Item("hagelbössa")
player_inventory.add_item(hagelbössa)

for item in player_inventory.get_contents():
    print(item)