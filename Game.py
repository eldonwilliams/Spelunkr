import AssetManager
import Input
import Material
import Registry
import PlayerData
import Area
import Globals
import EventHandler
from Registry import Registry as REG

class Game(REG):
    """
        Contains most modules of Spelunkr
        *extends of Registry*
    """
    def __init__(self):
        self.reg = {}
        self.registerItem('AssetManager', AssetManager)
        self.registerItem('Input', Input)
        self.registerItem('Material', Material)
        self.registerItem('Registry', Registry)
        self.registerItem('PlayerData', PlayerData)
        self.registerItem('Area', Area)
        self.registerItem('Globals', Globals)
        self.registerItem('EventHandler', EventHandler)