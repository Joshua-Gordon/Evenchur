from inventory import Inventory
from data import getLocation, getItemInLocation

import sys

class Evenchur:

    def __init__(self,loc):
        self.location = loc
        self.inv = Inventory()
        self.visitedLocations = []

    def loop(self):
        self.location = self.visited()
        print(self.location["desc"])
        inp = input(">>>").split(" ")
        if(inp[0] == "q"):
            print("Thank you for playing wing commander!")
            sys.exit(0)
        if(inp[0] == "go"):
            if inp[1] == "n" or inp[1] == "north":
                if self.location["name"] == self.location["north"]:
                    print("You cannot go that way.")
                else:
                    self.location = getLocation(self.location["north"])
            if inp[1] == "e" or inp[1] == "east":
                if self.location["name"] == self.location["east"]:
                    print("You cannot go that way.")
                else:
                    self.location = getLocation(self.location["east"])
            if inp[1] == "w" or inp[1] == "west":
                if self.location["name"] == self.location["west"]:
                    print("You cannot go that way.")
                else:
                    self.location = getLocation(self.location["west"])
            if inp[1] == "s" or inp[1] == "south":
                if self.location["name"] == self.location["south"]:
                    print("You cannot go that way.")
                else:
                    self.location = getLocation(self.location["south"])
        elif inp[0] == "items":
            print(self.inv)
        elif inp[0] == "look":
            if len(inp) == 1:
                print(self.location["look"])
                for i in self.location["items"]:
                    print("There is a " + str(i))
            else:
                i = getItemInLocation(inp[1].lower(),self.location)
                if i:
                    print(i.getDesc())
                else:
                    print("There is no " + inp[0] + " here!")
        elif inp[0] == "take":
            i = getItemInLocation(inp[1].lower(),self.location)
            if i:
                self.location["items"].remove(i.getName())
                self.inv.addItem(i)
                print("You take the " + str(i))
            else:
                print("There is no " + inp[0] + " here!")



    def visited(self):
        for l in self.visitedLocations:
            if l["name"] == self.location["name"]:
                return l
        return self.location
