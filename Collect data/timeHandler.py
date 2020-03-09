import datetime

class TimeHandler():
    def dateFormatted(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")