from datetime import datetime
from time import sleep
from fSequence import fSeq
import random

class klok:
    def __init__(self):
        # Initialize the time
        self.minute = datetime.now().minute / 5
        self.hour = datetime.now().hour
        if self.hour > 12:
            self.hour = self.hour - 12
        self.fHour, self.fMinute=self.fTime()

    def new_time(self):
        # Check if the difference between the time is 5 minutes
        minute = datetime.now().minute / 5
        if self.minute != minute:
            self.minute = minute
            self.hour = datetime.now().hour
            self.fHour, self.fMinute=self.fTime()
            return True
        else:
            return False
    def fTime(self):
        posFibDecom=fSeq(5)
        return random.choice(posFibDecom.fDecom[self.hour]), random.choice(posFibDecom.fDecom[self.minute])

if __name__ == '__main__':
    test = klok()
    print 'werkt'
    print 'Readable Time\t\t', datetime.now().hour, datetime.now().minute
    print 'Non Readable Time\t\t', test.hour, test.minute
    print 'Fib Hours\t', test.fHour
    print 'Fib Minutes\t', test.fMinute
    for i in range(1000):
        sleep(10)
        if test.new_time():
            print 'Nieuwe tijd'
            print 'Readable Time\t\t', datetime.now().hour, datetime.now().minute
            print 'Non Readable Time\t\t', test.hour, test.minute
            print 'Fib Hours\t', test.fHour
            print 'Fib Minutes\t', test.fMinute
