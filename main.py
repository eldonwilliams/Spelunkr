import Input
import time
import os
import importlib
from Game import Game
from Mods.BaseMod import Mod
from PlayerData import PlayerData
from Area import Area
from Material import Material
from Registry import Registry, MaterialRegistry, AreaRegistry, ModRegistry
from AssetManager import AssetManager
from Globals import Keys

game = Game()
playerData = PlayerData({})

def play():
    AssetManager.clearScreen()
    print(AssetManager.grabAsset('playMenu'))
    @Keys.hookKeyEventDecorator('r')
    def event(down):
        Keys.unhookAll()
        mainMenu()

def settings():
    def ModPage():
        AssetManager.clearScreen()
        print(AssetManager.grabAsset('modsMenu'))
        for mod in ModRegistry.reg:
            Info = ModRegistry.getItem(mod).Mod.info
            formated = 'ModName: {}\nModId: {}\nDescription: {}\nAuthor: {}'.format(Info["modname"], Info["modid"], Info["description"], Info["author"])
            print(AssetManager.generateBoxedText(formated))

    AssetManager.clearScreen()
    print(AssetManager.grabAsset('settingsMenu'))
    @Keys.hookKeyEventDecorator('r')
    def event(down):
        Keys.unhookAll()
        mainMenu()
    
    @Keys.hookKeyEventDecorator('m')
    def event(down):
        Keys.unhookAll()
        ModPage()


def mainMenu():
    AssetManager.clearScreen()
    print(AssetManager.grabAsset('mainMenu'))

    @Keys.hookKeyEventDecorator('p')
    def event(down):
        Keys.unhookAll()
        play()

    @Keys.hookKeyEventDecorator('e')
    def event(down):
        Keys.unhookAll()
        AssetManager.clearScreen()
        print('Thank you for playing')
        for num in range(0, 3):
            print('.')
            time.sleep(1)
        print('closing')
        os.abort()
    
    @Keys.hookKeyEventDecorator('s')
    def event(down):
        Keys.unhookAll()
        settings()

def main():
    AssetManager.clearScreen()
    Keys.start()

    for folder in os.listdir('./Mods'):
        Mod = importlib.import_module('.{}'.format(folder), package='Mods')
        ModRegistry.registerItem(folder, Mod)
        Mod.Mod.Load(game)
    Input.Input.genAliveThread()
    mainMenu()

main()