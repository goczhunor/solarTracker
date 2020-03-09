from protocol import SenzorReaderProtocol
import Adafruit_DHT

class TemperatureReader(SenzorReaderProtocol):
    # Class for storing readed values
    class ReadedValues():
        def __init__(self, temp, humidity):
            self.temp = temp
            self.humidity = humidity
    
    # ------ TemperatureReader implementation ------

    # Type DHT11
    senzorType = 11

    def __init__(self, senzorPin):
        self.senzorPin = senzorPin

    def setup(self):
        pass

    def read(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.senzorType, self.senzorPin)
        return self.ReadedValues(temperature, humidity)

