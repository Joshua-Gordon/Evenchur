from inventory import Inventory, Item
import data

from evenchur import Evenchur

DEBUG = True

inv = Inventory()

phoneData = data.items[0]
floppyData = data.items[1]

start = data.locations[0]

e = Evenchur(start)
while(True):
    if DEBUG:
        e.loop()
    else:
        try:
            e.loop()
        except:
            print("That didn't make sense, try again!")
