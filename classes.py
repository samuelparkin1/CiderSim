import random

######## fruit Classes #######
class Fruit():
    def __init__(self):
         self.flavour, self.colour = random.choice(self.varieties)
    def __repr__(self):
        return f"<{self.flavour}, {self.colour} , {self.__class__.__name__}>"

class Apple(Fruit):
    varieties = [("sour", "green"),("sweet", "red")]


class Pear(Fruit):
    varieties = [("mellow", "yellow"),("sharp", "green")]
    
######### tree Classes #####

class Tree():
    def __init__(self):
        self.fruits = []

    def __repr__(self):
        return f"{self.fruit_type.__name__} tree"

    def blossom(self):
        for i in range(self.fecundity):
            self.fruits.append(self.fruit_type())
            
    def harvest(self):
        crop = self.fruits
        self.fruits = []
        return crop                          

class Appletree(Tree):
    fecundity = 8
    fruit_type = Apple

class Peartree(Tree):
    fecundity = 5
    fruit_type = Pear

###########cider Classes#####

class Cider():
    def __init__(self, fruitlist):
        self.flavour = {
            "sweet": 0,
            "sour":0, 
            "mellow":0,
            "sharp": 0,}

        for fruit in fruitlist:
            self.flavour[fruit.flavour]+=1

    def __repr__(self):
        return f"a barrel of {max(self.flavour, key=lambda key: self.flavour[key])} cider"       