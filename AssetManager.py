import os

class AssetManager(object):
    """
    This class is ment to not be instanced. Please only use the static methods
    """
    @staticmethod
    def grabAsset(filename):
        """
            grab asset from assets that is a .txt
        """
        f = open('./assets/{}.txt'.format(filename))
        lines = f.readlines()
        string = ""
        f.close()
        for line in lines:
            string += line
        return string
    
    @staticmethod
    def clearScreen():
        """
            clears the terminal, used when switching menus
        """
        os.system('cls' if os.name == 'nt' else 'clear')