# coding=utf-8
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from databaseHandler import DatabaseHandler
import tkMessageBox

class ChartDrawer():
    # ------- CONSTANTS -------
    TIME = "time"
    MONO_VOLTAGE = "mono_voltage"
    MONO_CURRENT = "mono_current"
    POLY_VOLTAGE = "poly_voltage"
    POLY_CURRENT = "poly_current"
    TEMPERATURE = "temperature"
    HUMIDITY = "humidity"
    LIGHT = "light"

    def __init__(self, db_name):
        self.dbHandler = DatabaseHandler(db_name)

    # -------- Helper methods --------

    # Your 'dateString' should have the following format: %Y-%m-%d %H:%M:%S
    def __dateFrom(self, dateString):
        return datetime.datetime.strptime(dateString, '%Y-%m-%d %H:%M:%S')

    # Calculate max value with an extra 3% to see clearly the upper bounds of the plots
    def __calcMax(self, values):
        maxVal = max(values)
        return maxVal + maxVal * 3 / 100

    def __calcMin(self, values):
        minVal = min(values)
        return minVal - minVal * 5 / 100

    def __titleFor(self, colom):
        if colom == self.LIGHT:
            return "Lumina (lx)"
        elif colom == self.TEMPERATURE:
            return "Temperatura (C)"
        elif colom == self.HUMIDITY:
            return "Umiditate (%)"
        elif colom == self.POLY_VOLTAGE or colom == self.MONO_VOLTAGE:
            return "Tensiune (V)"
        elif colom == self.POLY_CURRENT or colom == self.MONO_CURRENT:
            return "Curent (mA)"

    # -------- Draw charts methods --------

    def drawFor(self, coloms, fromDate, toDate, chartTitle):
        xValues = []
        yValues = []
        for i in range(len(coloms) + 1):
            tempYvalues = []
            fetchedData = self.dbHandler.fetchRows(coloms, fromDate, toDate)
            for row in fetchedData:
                if i == 0:
                    xValues.append(row[0])
                else:
                    tempYvalues.append(row[i])
            if len(tempYvalues) > 0:
                yValues.append(tempYvalues)

        if len(yValues) == 0:
            tkMessageBox.showinfo('Eroare', 'Nu am găsit nici un rezultat. Vă rog să verificați dacă ați selectat un inerval de date unde aveți măsurători salvate.')
            return

        date = []
        for x in xValues:
            date.append(self.__dateFrom(x))

        fig = plt.figure()
        yValCount = len(yValues)
        for i in range(yValCount):
            subPlot = fig.add_subplot(yValCount, 1, i + 1)
            subPlot.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
            subPlot.grid(True)
            subPlot.set_ylim([self.__calcMin(yValues[i]), self.__calcMax(yValues[i])])
            subPlot.plot_date(date, yValues[i], "-", linewidth=1.5)
            subPlot.tick_params(labelbottom = i == yValCount-1)
            subPlot.set_ylabel(self.__titleFor(coloms[i]))
            subPlot.yaxis.tick_right()

        plt.suptitle(chartTitle)
        plt.grid(True)
        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.05, top=0.9, hspace=0.05)
        plt.show()

    # -------- DRAW CHARTS --------

    def drawTempMonoCurrent_sunny(self):
        coloms = [self.TEMPERATURE, self.MONO_CURRENT]
        data = ChartData("Temperatura cu curent monocristalin", chart1LabelX = "Timp", chart1LabelY = "Temp", chart2LabelX = "Timp", chart2LabelY = "Curent (mA)")
        self.draw3(coloms, "2019-06-02 13:00:57", "2019-06-02 17:30:16", data)

    def drawTempMonoVoltage_sunny(self):
        coloms = [self.TEMPERATURE, self.MONO_VOLTAGE]
        data = ChartData("Temperatura cu tensiune monocristalin")
        self.draw3(coloms, "2019-06-02 13:20:57", "2019-06-02 17:30:16", data)

    def drawTempPolyCurrent_sunny(self):
        coloms = [self.TEMPERATURE, self.MONO_CURRENT]
        data = ChartData("Temperatura cu curent policristalin", chart1LabelX="Timp", chart1LabelY="Temp", chart2LabelX="Timp", chart2LabelY="Curent (mA)")
        self.draw3(coloms, "2019-06-02 13:00:57", "2019-06-02 17:30:16", data)

    def drawTempPolyVoltage_sunny(self):
        coloms = [self.TEMPERATURE, self.POLY_CURRENT]
        data = ChartData("Temperatura cu tensiune policristalin")
        self.draw3(coloms, "2019-06-02 13:20:57", "2019-06-02 17:30:16", data)

    def drawLightPolyVoltage_sunny(self):
        coloms = [self.MONO_VOLTAGE, self.MONO_CURRENT, self.TEMPERATURE, self.HUMIDITY, self.LIGHT]
        self.drawFor(coloms, "2019-06-02 13:20:57", "2019-06-02 17:30:16", "Lumina cu tensiune policristalin")