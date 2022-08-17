from parser import PickleEncode



"""
Message class is for messages that 
are send and receive between server and client.
"""
class Message:
    """
    constructor.

    @param type: message type which can be (subscribe, unsubscribe or normal)
    """
    def __init__(self, type="normal", topic="", data=""):
        self.type = type
        self.topic = topic
        self.data = data

    """
    setTopic.

    @param topic: message topic.
    """
    def setTopic(self, topic):
        self.topic = topic
    
    """
    setData.

    @param data: message payload.
    """
    def setData(self, data):
        self.data = PickleEncode(data)
