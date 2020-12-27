import datetime
from .functions import getDayString

class moment:
    def __init__(self, dateString='', formatString=''):
        self.dateString = ''
        self.formatString = formatString
        if len(dateString) == 0:
            # Configuring Default
            self.day = datetime.datetime.now().day
            self.month = datetime.datetime.now().month
            self.year = datetime.datetime.now().year
            self.hour = datetime.datetime.now().hour
            self.minute = datetime.datetime.now().minute
            self.second = datetime.datetime.now().second
            self.micro_second = datetime.datetime.now().microsecond

    # __repr__ will have in displaying the normal Date
    def __repr__(self):
        return str(getDayString(3))