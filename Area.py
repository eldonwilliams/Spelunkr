import random
from Registry import Registry

class Area(object):
    """
        An Area is a place the player can be and contains materials the player can mine
    """
    def __init__(self, name, cost, modid):
        self.name = name
        self.modid = modid
        self.cost = cost
        self.Materials = Registry()

    def getRandomMaterial(self):
        """
            Returns a random material from self.Materials
        """
        materialArray = list(self.Materials.reg.values())
        return materialArray[random.randint(0, len(materialArray)-1)]