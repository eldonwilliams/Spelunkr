from Registry import Registry

class Area(object):
    """
        An Area is a place the player can be and contains materials the player can mine
    """
    def __init__(self, name, modid):
        self.name = name
        self.modid = modid
        self.Materals = Registry()


