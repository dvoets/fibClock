from datetime import datetime, timedelta
from time import sleep
from fSequence import fSeq
import random

class klok:
    def __init__(self, fadeTime, lightIntensity = 50):
        # Constant for fading
        # Initialize the time
        self.fadeTime = fadeTime
        self.lightIntensity = lightIntensity
        now = datetime.now() + timedelta(seconds=self.fadeTime)
        self.minute = now.minute / 5
        self.hour = now.hour

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
        self.prev_timeRGB = self.fTimeRGB()
        print 'RED \t= Hours'
        print 'GREEN \t= Minute'
        print 'BLUE \t= Hours AND Minute'
        print 'TIME NOW:', datetime.now()
        print 'Colors Time Now: ', self.timeColor
        print 'RGB Time Now: ', self.timeRGB

    def new_time(self):
        # Check if the difference between the time is 5 minutes
        now = datetime.now() + timedelta(seconds=self.fadeTime)
        minute = now.minute / 5
        if self.minute != minute:
            self.prev_hour = self.hour
            self.prev_minute = self.minute
            self.hour = now.hour
            self.minute = minute
            print self.hour, self.minute
            if self.hour > 12:
                self.hour = self.hour - 12
            self.fHour, self.fMinute = self.fTime()
            self.timeColor = self.fTimeColor()
            self.prev_timeRGB = self.timeRGB
            self.timeRGB = self.fTimeRGB()
            print 'NEW TIME', datetime.now()
            print 'Colors New Time: ', self.timeColor
            print 'RGB prev Time: ', self.prev_timeRGB
            print 'RGB New Time: ', self.timeRGB
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
                fRGB[i]= [0, 0, self.lightIntensity]
            #Green
            elif self.fMinute[i]:
                fRGB[i]= [0, self.lightIntensity, 0]
            #Red
            elif self.fHour[i]:
                fRGB[i]= [self.lightIntensity, 0, 0]
            #White
            else:
                fRGB[i]= [self.lightIntensity/3, self.lightIntensity/3, self.lightIntensity/3]
        return fRGB



if __name__ == '__main__':
    test = klok(120, 40)
    while True:
        if test.new_time():
            print 'NEW TIME'
