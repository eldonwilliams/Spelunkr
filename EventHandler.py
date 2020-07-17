from enum import Enum, auto

class Events(Enum):
    UnhookedAllKeyhooks = auto()

class EventHandler(object):
    """
        Subscribe Events that get called, mainly used for mods
    """
    def __init__(self):
        self.events = {}

    def hookEventDecorator(self, eventEnum):
        """
            Hook a event with a decorator and a event enum
        """
        def wrapper(function):
            if not eventEnum in self.events: self.events[eventEnum] = []
            self.events[eventEnum].append(function)
        return wrapper
    
    def fireEvent(self, eventEnum, *args):
        """
            Used internally to fire a event
        """
        if not eventEnum in self.events: return
        for event in self.events[eventEnum]:
            event(args)

MainHandler = EventHandler()