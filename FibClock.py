from datetime import datetime
from time import sleep
from fSequence import fSeq
import random

class klok:
    def __init__(self, fadeTime):
        # Constant for fading
        self.fadeTime = fadeTime
        # Initialize the time
        self.minute = datetime.now().minute / 5
        self.hour = datetime.now().hour

        # Rescale hours to 1-12
        if self.hour > 12:
            self.hour = self.hour - 12

        # Keep track of time on the previous period
        self.prev_minute = self.minute
        self.prev_hour = self.hour

        # Hours and Minutes each as a sum of fib numbers
        self.fHour, self.fMinute = self.fTime()
        # Fib time converted into colors (G=Hours, R=Minutes, B=Hours and Minutes)
        self.timeColor = self.fTimeColor()
        self.timeRGB = self.fTimeRGB() 

    def new_time(self):
        # Check if the difference between the time is 5 minutes
        minute = datetime.now().minute / 5
        if self.minute != minute:
            self.prev_hour = self.hour
            self.prev_minute = self.minute
            self.hour = datetime.now().hour
            self.minute = minute
            self.fHour, self.fMinute = self.fTime()
            self.timeColor = self.fTimeColor()
            self.timeRGB = self.fTimeRGB() 
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

    def fTimeRGB(self):
        fRGB = {}
        for i in range(5):
            #Blue
            if self.fMinute[i] and self.fHour[i]:
                fRGB[i]= [0, 0, 255]
            #Green
            elif self.fMinute[i]:
                fRGB[i]= [0, 255, 0]
            #Red
            elif self.fHour[i]:
                fRGB[i]= [255, 0, 0]
            #White
            else:
                fRGB[i]= [255, 255, 255]
        return fRGB



if __name__ == '__main__':
    test = klok(0)
    print test.timeColor
    print "Previous Time: ", test.prev_hour, ':', test.prev_minute
    print "New Time: ", test.hour, ':', test.minute
    print test.timeRGB
    while True:
        if test.new_time():
            print 'NEW TIME'
            print test.timeColor
            print "Previous Time: ", test.prev_hour, ':', test.prev_minute
            print "New Time: ", test.hour, ':', test.minute
            print test.timeRGB
