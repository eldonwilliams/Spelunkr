"""
    Registers all used things for the game
"""

class Registry(object):
    """
        Registry describes a thing that can register things
    """
    def __init__(self):
        self.reg = {}
    
    def registerItem(self, name, object):
        """
            Registers a thing then returns it
        """
        self.reg[name] = object
        return self.reg[name]
    
    def getItem(self, name):
        """
            Gets a registered item
        """
        return self.reg[name]
    
MaterialRegistry = Registry()
AreaRegistry = Registry()
ModRegistry = Registry()