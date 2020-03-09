from ina219 import INA219
from protocol import SenzorReaderProtocol

class OutputReader(SenzorReaderProtocol):
    # Class for storing readed values
    class ReadedValues():
        def __init__(self, voltage, current):
            self.voltage = voltage # Stored in Volts
            self.current = current # Stored in Amps

    # ------ OutputReader implementation ------

    def __init__(self, senzorAddress):
        self.__ina = INA219(shunt_ohms=0.1, max_expected_amps = 0.25, address = senzorAddress)
        
    def setup(self):
        self.__ina.configure(voltage_range = self.__ina.RANGE_16V,
                      gain = self.__ina.GAIN_AUTO,
                      bus_adc = self.__ina.ADC_128SAMP,
                      shunt_adc = self.__ina.ADC_128SAMP)

    def read(self):
        voltage = self.__ina.voltage()
        current = self.__ina.current()
        return self.ReadedValues(voltage, current)

    def sleep(self):
        self.__ina.sleep()

    def wakeUp(self):
        self.__ina.wake()

    def printReadedValues(self):
        print('Voltage: {0:0.1f} V'.format(self.__ina.voltage()))
        print('Current: {} mA'.format(self.__ina.current()))
        print('Power: {} W'.format(self.__ina.power()))