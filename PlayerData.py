import json

class PlayerData(object):
    """
        PlayerData represents the datamodel for data pertaining to the player
    """
    @staticmethod
    def generateFromJson(fileLocation):
        """
            Generates a PlayerData object from data given at the FileLocation
        """
        return PlayerData(json.load(open(fileLocation, 'r')), filename=fileLocation)

    @staticmethod
    def saveToJson(playerData, fileLocation):
        """
            Saves a given PlayerData object to a given FileLocation
        """
        f = open(fileLocation, 'w+')
        f.write(json.dumps(playerData.__dict__))
        f.close()

    def __init__(self, jsonData, filename=""):
        def get(key, other): return (jsonData[key] if key in jsonData else other)
        self.credits = get('Credits', 0)
        self.unlockedAreas = get('UnlockedAreas', [])
        self.filename = filename
        self.strength = get('Strength', 1)
        