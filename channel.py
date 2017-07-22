class Channel:

    def __init__(self, name, frequency, modulation, id):
        self.name = name
        self.frequency = frequency
        self.modulation = modulation
        self.id = id

    def getName(self):
        return self.name;

    def getFrequency(self):
        return self.frequency

    def getModulation(self):
        return self.modulation

    def getId(self):
        return self.id

    def __eq__(self, other):
        return ((self.lastfirst) == (other.name, other.first))

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.last, self.first) < (other.last, other.first))

    def __cmp__(self, other):
        return cmp( self.getName(), other.getName())