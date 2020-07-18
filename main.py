import Input
import time
import os
import importlib
import msvcrt
from Game import Game
from Mods.BaseMod import Mod
from PlayerData import PlayerData
from Area import Area
from Material import Material
from Registry import Registry, MaterialRegistry, AreaRegistry, ModRegistry
from AssetManager import AssetManager
from Globals import Keys, PD

game = Game()

def loadSave():
    selection = 0
    saves = os.listdir('./saves')

    def update():
        AssetManager.clearScreen()
        lsm = AssetManager.grabAsset('loadSaveMenu')
        
        if len(saves) > 0:
            saveStrings = "\n"
            i = 0
            for save in saves:
                saveStrings += save
                if i == selection:
                    saveStrings += " █"
                saveStrings += "\n"
                i += 1
        
            print(lsm.format(AssetManager.generateBoxedText(saveStrings)))
        else:
            print(lsm.format('empty\n'))

    @Keys.hookKeyEventDecorator('down')
    def event(down):
        nonlocal selection

        if not down: return
        if selection + 1 > len(saves) - 1:
            selection = 0
        else:
            selection += 1

        update()
    
    @Keys.hookKeyEventDecorator('up')
    def event(down):
        nonlocal selection

        if not down: return
        if selection - 1 < 0:
            selection = len(saves)-1
        else:
            selection -= 1
        
        update()
    
    @Keys.hookKeyEventDecorator('enter')
    def event(down):
        global PD

        if not down: return
        if len(saves) == 0: return
        PD = PlayerData.generateFromJson('./saves/{}'.format(saves[selection]))
        Keys.unhookAll()
        Input.Input.flushInput()
        print(PD.__dict__)
        print('data loaded')
        input('enter to continue')
        play()
        
    
    @Keys.hookKeyEventDecorator('r')
    def event(down):
        if not down: return
        Keys.unhookAll()
        saveManipulation()

    update()
    
def createSave():
    AssetManager.clearScreen()
    print(AssetManager.grabAsset('createSaveMenu'))

    @Keys.hookKeyEventDecorator('e')
    def event(down):
        if not down: return
        Keys.unhookAll()
        Input.Input.flushInput()
        newSaveLocation = './saves/{}.json'.format(input('save name: '))
        f = open(newSaveLocation, 'w+')
        f.write('{}')
        f.close()
        print('Created! Press enter to continue.')
        input()
        Keys.unhookAll()
        saveManipulation()
    
    @Keys.hookKeyEventDecorator('r')
    def event(down):
        if not down: return
        Keys.unhookAll()
        saveManipulation()

def saveManipulation():
    AssetManager.clearScreen()
    print(AssetManager.grabAsset('saveManipulationMenu'))

    @Keys.hookKeyEventDecorator('l')
    def event(down):
        if not down: return
        Keys.unhookAll()
        loadSave()

    @Keys.hookKeyEventDecorator('c')
    def event(down):
        if not down: return
        Keys.unhookAll()
        createSave()

    @Keys.hookKeyEventDecorator('r')
    def event(down):
        if not down: return
        Keys.unhookAll()
        mainMenu()

def areaSelection():
    selection = 0
    areas = []
    for area in AreaRegistry.reg: areas.append(AreaRegistry.getItem(area))

    def update():
        AssetManager.clearScreen()
        info = "\nCredits: {}\n".format(PD.credits)

        i = 0
        for area in areas:
            info += "{}{} Area: {} | Cost: {}c\n".format(("»" if selection == i else " "), ("▒" if area.name in PD.unlockedAreas else ("▓" if PD.credits >= area.cost else "█")), area.name, area.cost)
            i += 1
        
        string = AssetManager.grabAsset("areaSelectorMenu").format(AssetManager.generateBoxedText(info))
        print(string)
        
    @Keys.hookKeyEventDecorator('down')
    def event(down):
        nonlocal selection

        if not down: return
        if selection + 1 > len(areas) - 1:
            selection = 0
        else:
            selection += 1

        update()
    
    @Keys.hookKeyEventDecorator('up')
    def event(down):
        nonlocal selection

        if not down: return
        if selection - 1 < 0:
            selection = len(areas)-1
        else:
            selection -= 1
        
        update()
    
    @Keys.hookKeyEventDecorator('enter')
    def event(down):
        if not down: return
        selectedArea = areas[selection]

        if selectedArea.name in PD.unlockedAreas:
            #unlocked
            pass
        elif PD.credits >= selectedArea.cost:
            #unlock then set active
            pass
    
    update()

def play():
    AssetManager.clearScreen()
    
    if not PD:
        Keys.unhookAll()
        saveManipulation()
        return
    
    areaSelection()

def settings():
    def ModPage():
        AssetManager.clearScreen()
        modsMenu = AssetManager.grabAsset('modsMenu')
        long = ''
        for mod in ModRegistry.reg:
            Info = ModRegistry.getItem(mod).Mod.info
            formated = 'ModName: {}\nModId: {}\nDescription: {}\nAuthor: {}'.format(Info["modname"], Info["modid"], Info["description"], Info["author"])
            long += AssetManager.generateBoxedText(formated)
        print(modsMenu.format(long))

        @Keys.hookKeyEventDecorator('r')
        def event(down):
            if not down: return
            Keys.unhookAll()
            settings()

    AssetManager.clearScreen()
    print(AssetManager.grabAsset('settingsMenu'))
    @Keys.hookKeyEventDecorator('r')
    def event(down):
        if not down: return
        Keys.unhookAll()
        mainMenu()
    
    @Keys.hookKeyEventDecorator('m')
    def event(down):
        if not down: return
        Keys.unhookAll()
        ModPage()


def mainMenu():
    AssetManager.clearScreen()
    print(AssetManager.grabAsset('mainMenu'))

    @Keys.hookKeyEventDecorator('p')
    def event(down):
        if not down: return
        Keys.unhookAll()
        play()

    @Keys.hookKeyEventDecorator('e')
    def event(down):
        if not down: return
        Keys.unhookAll()
        AssetManager.clearScreen()
        print('Thank you for playing')
        if PD: PlayerData.saveToJson(PD, PD.filename)
        for num in range(0, 3):
            print('.')
            time.sleep(1)
        print('closing')
        os.abort()
    
    @Keys.hookKeyEventDecorator('s')
    def event(down):
        if not down: return
        Keys.unhookAll()
        settings()

def main():
    AssetManager.clearScreen()
    Keys.start()

    for folder in os.listdir('./Mods'):
        print(folder)
        Mod = importlib.import_module('.{}'.format(folder), package='Mods')
        ModRegistry.registerItem(folder, Mod)
        for asset in os.listdir('./Mods/{}/assets'.format(folder)):
            f = open('./assets/{}'.format(asset), 'w+')
            f.writelines(open('./Mods/{}/assets/{}'.format(folder, asset)).readlines())
            f.close()
        Mod.Mod.Load(game)
    Input.Input.genAliveThread()
    mainMenu()

main()