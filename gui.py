import tkinter
from inventory import Inventory, Item

player_inventory = Inventory()

main = tkinter.Tk()

label = tkinter.Label(main, text="Hello")
label.pack()
inputbox = tkinter.Entry(main)
inputbox.pack(pady=20)

def log(itemName):
    for item in player_inventory.get_contents():
        textbox.insert(tkinter.END, item.name + "\n")

def CreatenAdd(event = None):
    itemName = inputbox.get()
    Inventory.add_item(Item(inputbox.get()), 0)
    log(itemName)

button = tkinter.Button(main, text="Add Item", command=CreatenAdd)
button.pack(pady=20)
textbox = tkinter.Text(main, height=10, width = 40)
textbox.pack(pady=20)

main.mainloop()