import smbus
from protocol import SenzorReaderProtocol

class LightReader(SenzorReaderProtocol):
    __ONE_TIME_HIGH_RES_MODE_1 = 0x10
    
    def setup(self):
        self.bus = smbus.SMBus(1)

    def read(self):
        # delay of 0.5 sec is needed after every read
        data = self.bus.read_i2c_block_data(self.senzorAddress, self.__ONE_TIME_HIGH_RES_MODE_1)
        return self.__convertToNumber(data)
        
    def __convertToNumber(self, data):
        return ((data[1] + (256 * data[0])) / 1.2)