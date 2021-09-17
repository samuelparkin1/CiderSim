import random

######## fruit Classes #######
class Fruit():
     def __init__(self):
         self.flavour, self.colour = random.choice(self.varieties)

class Apple(Fruit):
    varieties = [("sour", "green"),("sweet", "Red")]


class Pear(Fruit):
    varieties = [("mellow", "yellow"),("sharp", "Green")]
    
######### tree Classes #####

class Tree():
    def __init__(self):
        self.fruits = []

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
            

        }