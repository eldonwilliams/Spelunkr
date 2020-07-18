import os

class AssetManager(object):
    """
    This class is ment to not be instanced. Please only use the static methods
    """
    @staticmethod
    def rawGrabAsset(filelocation):
        """
            grbas a asset from a file location rather than the ./assets/{}.txt
        """
        f = open(filelocation, encoding='utf-8')
        lines = f.readlines()
        string = ""
        f.close()
        for line in lines:
            string += line
        return string
        

    @staticmethod
    def grabAsset(filename):
        """
            grab asset from assets that is a .txt
        """
        return AssetManager.rawGrabAsset('./assets/{}.txt'.format(filename))
    
    @staticmethod
    def generateBoxedText(message):
        """
            Generates a boxed message
        """
        splitMessage = message.split('\n')
        longestSegment = None
        for section in splitMessage:
            if len(section) >= len(longestSegment or section):
                longestSegment = section
        string = "+={}=+\n".format(len(longestSegment)*"=")
        for section in splitMessage:
            string += "| {}{} |\n".format(section, (len(longestSegment)-len(section))*" ")
        string += "+={}=+\n".format(len(longestSegment)*"=")
        return string
    
    @staticmethod
    def saveAsset(assetFile, newName):
        """
            Pushes data from a filelocation to a .txt in assets 
        """
        f = open('./assets/{}.txt'.format(newName), 'w+')
        f.writelines(assetFile.readlines())
        f.close()

    @staticmethod
    def clearScreen():
        """
            clears the terminal, used when switching menus
        """
        os.system('cls' if os.name == 'nt' else 'clear')