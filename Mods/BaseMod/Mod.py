"""
    Index for the base mod
"""

info = {
    "modname": "Spelunkr",
    "modid": "spelunkr",
    "description": "Spelunkr's base game assets.",
    "author": "Spelunkr Team"
}

def Load(game):
    Area = game.getItem("Area")
    Material = game.getItem("Material")
    AssetManager = game.getItem("AssetManager")
    Registry = game.getItem("Registry")

    MaterialRegistry = Registry.MaterialRegistry
    AreaRegistry = Registry.AreaRegistry

    forestArea = Area.Area(name='The Forest', modid=info["modid"], cost=0)
    testArea1 = Area.Area(name='TA1', modid=info["modid"], cost=10)
    testArea2 = Area.Area(name='TA2', modid=info["modid"], cost=75)
    pebbleMaterial = Material.Material(name='Pebble', health=10, area=forestArea, value=1, asset='pebble', modid=info["modid"])

    MaterialRegistry.registerItem(pebbleMaterial.name, pebbleMaterial)
    AreaRegistry.registerItem(forestArea.name, forestArea)
    AreaRegistry.registerItem(testArea1.name, testArea1)
    AreaRegistry.registerItem(testArea2.name, testArea2)