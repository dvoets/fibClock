from datetime import datetime
from time import sleep
from fSequence import fSeq
import random

class klok:
    def __init__(self, fadeTime):
        # Initialize the time
        self.minute = datetime.now().minute / 5
        self.hour = datetime.now().hour
        if self.hour > 12:
            self.hour = self.hour - 12
        self.fHour, self.fMinute=self.fTime()
        self.fadeTime = fadeTime
        self.timeColor = self.fTimeColor()

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

    def fTimeColor(self):
        timeColor = ['W','W', 'W', 'W', 'W']
        for i in range(len(self.fHour)):
            if self.fMinute[i] and self.fHour[i]:
                timeColor[i]='B'
            elif self.fMinute[i]:
                timeColor[i]='G'
            elif self.fHour[i]:
                timeColor[i]='R'
        return timeColor



if __name__ == '__main__':
    test = klok(0)
    print 'Fade Time: ', test.fadeTime
    print 'werkt'
    print test.timeColor
    print '------------------'
    print '|2 2 0 4 4 4 4 4 |'
    print '|2 2 1 4 4 4 4 4 |'
    print '|3 3 3 4 4 4 4 4 |'
    print '|3 3 3 4 4 4 4 4 |'
    print '|3 3 3 4 4 4 4 4 |'
    print '------------------'
    print 'Readable Time\t\t', datetime.now().hour, datetime.now().minute
    print 'Non Readable Time\t', test.hour, test.minute
    print 'Fib Hours\t', test.fHour
    print 'Fib Minutes\t', test.fMinute
    while True:
        if test.new_time():
            print 'Nieuwe tijd'
            print 'Readable Time\t\t', datetime.now().hour, datetime.now().minute
            print 'Non Readable Time\t\t', test.hour, test.minute
            print 'Fib Hours\t', test.fHour
            print 'Fib Minutes\t', test.fMinute
            print test.timeColor
