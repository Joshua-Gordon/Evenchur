class Inventory:
    def __init__(self):
        self.items = []
        self.weight = 0
        self.maxWeight = 20

    def getItems(self):
        return self.items
    def getWeight(self):
        return self.weight
    def getMaxWeight(self):
        return self.maxWeight

    def addItem(self,item):
        if self.weight + item.getWeight() < self.maxWeight:
            if item in self.items:
                idx = self.items.index(item)
                self.items[idx].increment()
            else:
                self.items.append(item)

    def item(self,name):
        for i in self.items:
            if i.getName() == name:
                return i

    def __str__(self):
        toreturn = "Inventory:\n"
        for i in self.items:
            toreturn += "x"+str(i.getCount()) + "\t" + i.getName() + "\n"
        return toreturn





class Item:
    def __init__(self,**kwargs):
        #print(kwargs)
        self.name = kwargs['name']
        self.desc = kwargs['desc']
        self.weight = kwargs['weight']
        if "count" in kwargs.keys():
            self.count = kwargs['count']
        else:
            self.count = 1
    def getName(self):
        return self.name
    def getDesc(self):
        return self.desc
    def getWeight(self):
        return self.weight
    def getCount(self):
        return self.count

    def increment(self):
        self.count += 1

    def __eq__(self,other):
        return self.name == other.getName()
    def __str__(self):
        return self.name
