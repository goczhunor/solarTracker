# This protocol is the base class of every senzor reader class.
class SenzorReaderProtocol():
    # Init
    def __init__(self, senzorAddress = None):
        self.senzorAddress = senzorAddress

    # Protocol methods
    def setup(self):
        raise NotImplementedError(self.__notConformError(self.setup.__name__))
    def read(self):
        raise NotImplementedError(self.__notConformError(self.read.__name__))

    # Private helper methods
    def __notConformError(self, methodName):
        return "Your class is not conform {}. Implement '{}()' to make it conform the protocol.".format(self.__className(), methodName)

    def __className(self):
        for base in self.__class__.__bases__:
            return base.__name__