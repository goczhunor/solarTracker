from temperatureReader import TemperatureReader
from lightReader import LightReader
from outputReader import OutputReader
from timeHandler import TimeHandler
from databaseHandler import DatabaseHandler
import time

# ---------- CONSTANTS ----------
TEMP_SENZOR_PIN = 4
LIGHT_SENZOR_ADDRESS = 0X23
CURENT_SENZOR_MONO_ADDRESS = 0x40
CURENT_SENZOR_POLY_ADDRESS = 0x41
DATABASE_LOCATION = "measurements.db"
DELAY_BETWEEN_READINGS = 600 # 600 sec = 10 min

class FlowHandler():
    tempReader = TemperatureReader(TEMP_SENZOR_PIN)
    lightReader = LightReader(LIGHT_SENZOR_ADDRESS)
    curentReaderMono = OutputReader(CURENT_SENZOR_MONO_ADDRESS)
    curentReaderPoly = OutputReader(CURENT_SENZOR_POLY_ADDRESS)
    databaseHandler = DatabaseHandler(DATABASE_LOCATION)

    def setup(self):
        self.lightReader.setup()
        self.curentReaderMono.setup()
        self.curentReaderPoly.setup()
        self.databaseHandler.createTableIfNeeded()

    def readAndSaveDataIfNeeded(self):
        light = self.lightReader.read()

        # Early escape if it's completely dark outside.
        if light < 1:
            return

        valuesFromTempSenzor = self.tempReader.read()
        valuesFromMono = self.curentReaderMono.read()
        valuesFromPoly = self.curentReaderPoly.read()

        self.databaseHandler.saveData(self.formatted(valuesFromMono.voltage),
                                      self.formatted(valuesFromMono.current),
                                      self.formatted(valuesFromPoly.voltage),
                                      self.formatted(valuesFromPoly.current),
                                      self.formatted(valuesFromTempSenzor.temp),
                                      self.formatted(valuesFromTempSenzor.humidity),
                                      self.formatted(light))

    def wakeUpSenzors(self):
        self.curentReaderMono.wakeUp()
        self.curentReaderPoly.wakeUp()

    def sleepSensors(self):
        self.curentReaderMono.sleep()
        self.curentReaderPoly.sleep()
        
    # Returns the 'value' formatted to have 4 decimals only.
    def formatted(self, value):
        return '{0:.4f}'.format(value)
        


flowHandler = FlowHandler()
flowHandler.setup()

while True:
    flowHandler.wakeUpSenzors()
    flowHandler.readAndSaveDataIfNeeded()
    flowHandler.sleepSensors()
    time.sleep(DELAY_BETWEEN_READINGS)
