from AssetManager import AssetManager

class Material(object):
    """
        Contains information about a given material
        A material is a object that can be mined in a given Area
    """
    def __init__(self, name, health, area, value, asset, modid):
        self.name = name
        self.area = area
        self.asset = asset
        self.health = health
        self.art = AssetManager.grabAsset(asset)
        self.value = value
        self.modid = modid
        self.area.Materials.registerItem(self.name, self)