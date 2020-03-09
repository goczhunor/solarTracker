import sqlite3
from timeHandler import TimeHandler

class DatabaseHandler:
    __timeHandler = TimeHandler()
    TIME_FIELD = "time"

    def __init__(self, dbName):
        self.dbName = dbName
        self.openDatabase()
        self.cursor = self.connection.cursor()

    def openDatabase(self):
        self.connection = sqlite3.connect(self.dbName + ".db")

    def closeDatabase(self):
        self.connection.close()

    def createTableIfNeeded(self):
        sql_create_measurements_table = """CREATE TABLE IF NOT EXISTS {} (
                                            time string PRIMARY KEY,
                                            mono_voltage double,
                                            mono_current double,
                                            poly_voltage double,
                                            poly_current double,
                                            temperature double,
                                            humidity double,
                                            light double
                                        );""".format(self.dbName)
        self.cursor.execute(sql_create_measurements_table)

    def saveData(self, mono_voltage, mono_current, poly_voltage, poly_current, temperature, humidity, light):
        currentTime = self.__timeHandler.dateFormatted()
        values = [(currentTime, mono_voltage, mono_current, poly_voltage, poly_current, temperature, humidity, light)]
        self.cursor.executemany('INSERT INTO {} VALUES (?,?,?,?,?,?,?,?)'.format(self.dbName), values)
        self.connection.commit()

    # ---------- FETCH ----------

    def fetchRowsFrom(self, coloms):
        query = "SELECT "
        nrElements = len(coloms)
        for i in range(nrElements):
            query += coloms[i]
            if(nrElements - 1 > i):
                query += ", "

        query += " FROM " + self.dbName
        return self.cursor.execute(query)

    def fetchRows(self, coloms, fromDate, toDate):
        query = "SELECT {}, ".format(self.TIME_FIELD)
        nrElements = len(coloms)
        for i in range(nrElements):
            query += coloms[i]
            if (nrElements - 1 > i):
                query += ", "

        query += " FROM {} WHERE {} BETWEEN '{}' AND '{}'".format(self.dbName, self.TIME_FIELD, fromDate, toDate)
        return self.cursor.execute(query)