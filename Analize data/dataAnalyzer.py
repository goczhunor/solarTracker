# coding=utf-8
import datetime
import calendar
from chartDrawer import ChartDrawer
import tkMessageBox
from ttk import *
from Tkinter import *

class DataAnalyzer():
    __MONO = "Monocristalin"
    __POLY = "Policristalin"

    drawer = ChartDrawer("measurements")

    def __init__(self):
        self.window = Tk()
        self.titleInputField = Entry(self.window, width = 30)
        self.combo = Combobox(self.window)
        self.button = Button(self.window, text="Afișează grafic", command = self.buttonClicked, background="Blue")
        self.setupUI()

    def showWindow(self):
        self.window.mainloop()

    def setupUI(self):
        self.__setupWindow()
        self.__addTitleInputField()
        self.__addComboBox()
        self.__addCheckBoxes()
        self.__addButton()
        self.__addDatePickers()


    def __setupWindow(self):
        self.window.title("Analizor de date")
        self.window.geometry('850x300')

    def __addTitleInputField(self):
        Label(self.window, text="Titlul graficelor").grid(column = 0, row = 0)
        self.titleInputField.grid(column = 0, row = 1)

    def __addComboBox(self):
        self.combo['values'] = (self.__MONO, self.__POLY)
        self.combo.current(1)  # set the selected item
        self.combo.grid(column = 0, row = 2)

    def __addCheckBoxes(self):
        column = 10
        alignment = "W" # aligned to left (West)

        self.chkCurentValue = BooleanVar()
        chkCurent = Checkbutton(self.window, text='Curent', var = self.chkCurentValue)
        chkCurent.grid(column = column, row = 0, sticky = alignment)
        chkCurent.select()

        self.chkVoltageValue = BooleanVar()
        chkVoltage = Checkbutton(self.window, text='Tensiune', var = self.chkVoltageValue)
        chkVoltage.grid(column = column, row = 1, sticky = alignment)
        chkVoltage.select()

        self.chkTempValue = BooleanVar()
        chkTemp = Checkbutton(self.window, text='Temperatură', var = self.chkTempValue)
        chkTemp.grid(column = column, row = 2, sticky = alignment)
        chkTemp.select()

        self.chkHumidityValue = BooleanVar()
        chkHumidity = Checkbutton(self.window, text='Umiditate', var = self.chkHumidityValue)
        chkHumidity.grid(column = column, row = 3, sticky = alignment)
        chkHumidity.select()

        self.chkLightValue = BooleanVar()
        chkLight = Checkbutton(self.window, text='Lumină', var = self.chkLightValue)
        chkLight.grid(column = column, row = 4, sticky = alignment)
        chkLight.select()

    def __addButton(self):
        self.button.grid(column = 0, row = 5)

    def __addDatePickers(self):
        currentDate = datetime.datetime.now()
        currentYear = currentDate.year
        currentMonth = currentDate.month
        fromRow = 1
        toRow = 3

        # ------ FROM DATE PICKER ------
        Label(self.window, text="De la").grid(column=1, row=fromRow - 1)
        self.fromDayVar = IntVar()
        self.fromDayVar.set(currentDate.day)
        fromDaySpin = Spinbox(self.window, from_=1, to=calendar.monthrange(currentDate.year, currentDate.month)[1], width=5, textvariable=self.fromDayVar)
        fromDaySpin.grid(column=1, row=fromRow, sticky=W + E)
        Label(self.window, text="-").grid(column=2, row=fromRow)
        self.fromMonthVar = IntVar()
        self.fromMonthVar.set(currentMonth)
        fromMonthSpin = Spinbox(self.window, from_=1, to=12, width=3, textvariable=self.fromMonthVar)
        fromMonthSpin.grid(column=3, row=fromRow, sticky=W + E)
        Label(self.window, text="-").grid(column=4, row=fromRow)
        self.fromYearVar = IntVar()
        self.fromYearVar.set(currentYear)
        fromYearSpin = Spinbox(self.window, from_ = currentYear - 5, to = currentYear, width=5, textvariable = self.fromYearVar)
        fromYearSpin.grid(column = 5, row = fromRow, sticky=W+E)
        Label(self.window, text=" ").grid(column=6, row=fromRow)
        self.fromHourVar = IntVar()
        self.fromHourVar.set(currentDate.hour)
        fromHourSpin = Spinbox(self.window, from_ = 0, to = 23, width=5, textvariable = self.fromHourVar)
        fromHourSpin.grid(column = 7, row = fromRow, sticky=W+E)
        Label(self.window, text=":").grid(column=8, row=fromRow)
        self.fromMinVar = IntVar()
        self.fromMinVar.set(currentDate.minute)
        fromMinSpin = Spinbox(self.window, from_ = 0, to = 59, width=5, textvariable = self.fromMinVar)
        fromMinSpin.grid(column = 9, row = fromRow, sticky=W+E)

        # ------ TO DATE PICKER ------
        Label(self.window, text="Până la").grid(column=1, row=toRow - 1)
        self.toDayVar = IntVar()
        self.toDayVar.set(currentDate.day)
        toDaySpin = Spinbox(self.window, from_=1, to=calendar.monthrange(currentDate.year, currentDate.month)[1], width=5, textvariable=self.toDayVar)
        toDaySpin.grid(column=1, row=toRow, sticky=W + E)
        Label(self.window, text="-").grid(column=2, row=toRow)
        self.toMonthVar = IntVar()
        self.toMonthVar.set(currentMonth)
        toMonthSpin = Spinbox(self.window, from_=1, to=12, width=3, textvariable=self.toMonthVar)
        toMonthSpin.grid(column=3, row=toRow, sticky=W + E)
        Label(self.window, text="-").grid(column=4, row=toRow)
        self.toYearVar = IntVar()
        self.toYearVar.set(currentYear)
        toYearSpin = Spinbox(self.window, from_=currentYear - 5, to=currentYear, width=3, textvariable=self.toYearVar)
        toYearSpin.grid(column=5, row=toRow, sticky=W + E)
        Label(self.window, text=" ").grid(column=6, row=toRow)
        self.toHourVar = IntVar()
        self.toHourVar.set(currentDate.hour)
        toHourSpin = Spinbox(self.window, from_=0, to=23, width=3, textvariable=self.toHourVar)
        toHourSpin.grid(column=7, row=toRow, sticky=W + E)
        Label(self.window, text=":").grid(column=8, row=toRow)
        self.toMinVar = IntVar()
        self.toMinVar.set(currentDate.minute)
        toMinSpin = Spinbox(self.window, from_=0, to=59, width=3, textvariable=self.toMinVar)
        toMinSpin.grid(column=9, row=toRow, sticky=W + E)

    def getFromDate(self):
        month = self.addZeroIfNeeded(self.fromMonthVar.get())
        day = self.addZeroIfNeeded(self.fromDayVar.get())
        hour = self.addZeroIfNeeded(self.fromHourVar.get())
        min = self.addZeroIfNeeded(self.fromMinVar.get())
        dateText = "{}-{}-{} {}:{}:00".format(self.fromYearVar.get(), month, day, hour, min)
        return dateText

    def getToDate(self):
        month = self.addZeroIfNeeded(self.toMonthVar.get())
        day = self.addZeroIfNeeded(self.toDayVar.get())
        hour = self.addZeroIfNeeded(self.toHourVar.get())
        min = self.addZeroIfNeeded(self.toMinVar.get())
        dateText = "{}-{}-{} {}:{}:00".format(self.toYearVar.get(), month, day, hour, min)
        return dateText

    def addZeroIfNeeded(self, value):
        if value < 10:
            return "0{}".format(value)
        return value

    def getColoms(self):
        coloms = []
        comboSelection = self.combo.get()
        if comboSelection == self.__POLY:
            if self.chkCurentValue.get():
                coloms.append("poly_current")
            if self.chkVoltageValue.get():
                coloms.append("poly_voltage")
        else:
            if self.chkCurentValue.get():
                coloms.append("mono_current")
            if self.chkVoltageValue.get():
                coloms.append("mono_voltage")

        if self.chkTempValue.get():
            coloms.append("temperature")
        if self.chkHumidityValue.get():
            coloms.append("humidity")
        if self.chkLightValue.get():
            coloms.append("light")

        return coloms

    def buttonClicked(self):
        coloms = self.getColoms()
        if len(coloms) == 0:
            tkMessageBox.showinfo('Eroare', 'Măcar o optiune trebuie să fie bifată.')
            return
        chartTitle = self.titleInputField.get()
        self.drawer.drawFor(coloms, self.getFromDate(), self.getToDate(), chartTitle)
        # self.drawer.drawFor(coloms, "2019-06-02 13:20:57", "2019-06-02 17:30:16", chartTitle)


test = DataAnalyzer()
test.showWindow()
