from inventory import Item

locations = [{
    "name" : "start",
    "desc" : "You are at the starting location",
    "look" : "This is the entrance of the computational singularity. You are standing in a small violet sphere of pulsing energy; the center of which, to the south, leads back to the SERVER ROOM.\n "
    + "To the north is a bright PORTAL that you cannot see through.",
    "north" : "portal0",
    "east" : "start",
    "west" : "start",
    "south" : "server room",
    "items" : ["lambda"]
}]

def getLocation(name):
    for l in locations:
        if l["name"] == name:
            return l
    print("Nonexistent location '" + name +"'")

def getItemInLocation(name,room):
    items = room["items"]
    if name in items:
        return getItem(name)

items = [
{
    "name" : "Rotary phone",
    "desc" : "This iPhone cannot physically stop rotating",
    "weight" : 0.1
},
{
    "name" : "Fuchsia floppy",
    "desc" : "110%% Go, crammed into 8kb",
    "weight": 0.05
},
{
    "name" : "lambda",
    "desc" : "A lambda abstraction. Allows you to use objects in the world.",
    "weight" : 1
}
]

def getItem(name):
    for i in items:
        if i["name"].lower() == name:
            return Item(**i)
    print("Nonexistent item '" + name + "'")
