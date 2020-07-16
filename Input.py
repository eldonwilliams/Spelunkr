import keyboard
import threading
import time

class Input(object):
    @staticmethod
    def genAliveThread():
        """
            creates then runs a thread to keep the process from exiting
            then returns it
        """

        def func(): time.sleep(999999)

        aliveThread = threading.Timer(9999, func)
        aliveThread.start()
        return aliveThread

    def __init__(self):
        self.KeysDown = []
        self.KeyHooks = {}
    
    def hookKeyEventDecorator(self, keyname):
        """
            hooks a key using a decorator
            @Input.hookKeyEventDecorator(keyname)
        """
        def wrapper(function):
            self.KeyHooks[keyname] = function
        return wrapper
    
    def hookKeyEvent(self, function, keyname):
        """
            hooks a predefined function to a key, it's recommended to use decorators
        """
        self.KeyHooks[keyname] = function
    
    def unhookKey(self, keyname):
        """
            unhooks a key event then returns the function if exists
        """
        if keyname in self.KeyHooks:
            save = self.KeyHooks[keyname]
            del self.KeyHooks[keyname]
            return save
        else:
            return None
    
    def unhookAll(self):
        """
            unhooks ALL key events
        """
        self.KeyHooks = {}

    def start(self):
        """
            starts listening to key presses and keyhooks
        """

        def keypress(e):
            down = keyboard.is_pressed(e.name)

            if down:
                if e.name in self.KeysDown: return
                self.KeysDown.append(e.name)
                if e.name in self.KeyHooks: self.KeyHooks[e.name](down)
            elif not down:
                if e.name in self.KeysDown: self.KeysDown.remove(e.name)
                if e.name in self.KeyHooks: self.KeyHooks[e.name](down)
        
        keyboard.hook(keypress)
