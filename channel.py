class Channel:

    def __init__(self, name, frequency, modulation, channel_id):
        self.name = name
        self.frequency = frequency
        self.modulation = modulation
        self.channel_id = channel_id

    def getName(self):
        return self.name

    def getFrequency(self):
        return self.frequency

    def getModulation(self):
        return self.modulation

    def getChannelId(self):
        return self.channel_id
