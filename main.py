import Input
import time
import os
from AssetManager import AssetManager

keys = None

def play():
    AssetManager.clearScreen()
    print(AssetManager.grabAsset('playMenu'))
    @keys.hookKeyEventDecorator('r')
    def event(down):
        keys.unhookAll()
        mainMenu()

def settings():
    AssetManager.clearScreen()
    print(AssetManager.grabAsset('settingsMenu'))
    @keys.hookKeyEventDecorator('r')
    def event(down):
        keys.unhookAll()
        mainMenu()

def mainMenu():
    AssetManager.clearScreen()
    print(AssetManager.grabAsset('mainMenu'))

    @keys.hookKeyEventDecorator('p')
    def event(down):
        keys.unhookAll()
        play()

    @keys.hookKeyEventDecorator('e')
    def event(down):
        keys.unhookAll()
        AssetManager.clearScreen()
        print('Thank you for playing')
        for num in range(0, 3):
            print('.')
            time.sleep(1)
        print('closing')
        os.abort()
    
    @keys.hookKeyEventDecorator('s')
    def event(down):
        keys.unhookAll()
        settings()
        
        

def main():
    AssetManager.clearScreen()
    global keys
    keys = Input.Input()
    keys.start()
    Input.Input.genAliveThread()
    mainMenu()

main()