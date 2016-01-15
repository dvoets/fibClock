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
        self.fTimeRGB = self.fTimeRGB() 

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
            self.fTimeRGB = self.fTimeRGB() 
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
        fTimeRGB = [[0] * 5] * 3
        for i in range(5):
            if self.fMinute[i] and self.fHour[i]:
                fTimeRGB[2][i] = 255
            elif self.fMinute[i]:
                fTimeRGB[1][i] = 255
            elif self.fHour[i]:
                fTimeRGB[0][i] = 255
        return fTimeRGB



if __name__ == '__main__':
    test = klok(0)
    print test.timeColor
    print "Previous Time: ", test.prev_hour, ':', test.prev_minute
    print "New Time: ", test.hour, ':', test.minute
    print test.fTimeRGB
    '''
    print 'Fade Time: ', test.fadeTime
    print 'werkt'
    print test.timeColor
    print '+---------------------+'
    print '|', test.timeColor[2],  test.timeColor[2],  '|', test.timeColor[0], '|',  test.timeColor[4],  test.timeColor[4],  test.timeColor[4],  test.timeColor[4],  test.timeColor[4], '|'
    print '+     +---+           +'
    print '|', test.timeColor[2],  test.timeColor[2],  '|', test.timeColor[1], '|',  test.timeColor[4],  test.timeColor[4],  test.timeColor[4],  test.timeColor[4],  test.timeColor[4], '|'
    print '+-----+---+           +'
    print '|', test.timeColor[3],  test.timeColor[3],  ' ', test.timeColor[3], '|',  test.timeColor[4],  test.timeColor[4],  test.timeColor[4],  test.timeColor[4],  test.timeColor[4], '|'
    print '|                     |'
    print '|', test.timeColor[3],  test.timeColor[3],  ' ', test.timeColor[3], '|',  test.timeColor[4],  test.timeColor[4],  test.timeColor[4],  test.timeColor[4],  test.timeColor[4], '|'
    print '|                     |'
    print '|', test.timeColor[3],  test.timeColor[3],  ' ', test.timeColor[3], '|',  test.timeColor[4],  test.timeColor[4],  test.timeColor[4],  test.timeColor[4],  test.timeColor[4], '|'
    print '+---------------------+'
    print 'Readable Time\t\t', datetime.now().hour, datetime.now().minute
    print 'Non Readable Time\t', test.hour, test.minute
    print 'Fib Hours\t', test.fHour
    print 'Fib Minutes\t', test.fMinute
    '''
    while True:
        if test.new_time():
            print test.timeColor
            print "Previous Time: ", test.prev_hour, ':', test.prev_minute
            print "New Time: ", test.hour, ':', test.minute
            print test.fTimeRGB
            '''
            print '+---------------------+'
            print '|', test.timeColor[2],  test.timeColor[2],  '|', test.timeColor[0], '|',  test.timeColor[4],  test.timeColor[4],  test.timeColor[4],  test.timeColor[4],  test.timeColor[4], '|'
            print '+     +---+           +'
            print '|', test.timeColor[2],  test.timeColor[2],  '|', test.timeColor[1], '|',  test.timeColor[4],  test.timeColor[4],  test.timeColor[4],  test.timeColor[4],  test.timeColor[4], '|'
            print '+-----+---+           +'
            print '|', test.timeColor[3],  test.timeColor[3],  ' ', test.timeColor[3], '|',  test.timeColor[4],  test.timeColor[4],  test.timeColor[4],  test.timeColor[4],  test.timeColor[4], '|'
            print '|                     |'
            print '|', test.timeColor[3],  test.timeColor[3],  ' ', test.timeColor[3], '|',  test.timeColor[4],  test.timeColor[4],  test.timeColor[4],  test.timeColor[4],  test.timeColor[4], '|'
            print '|                     |'
            print '|', test.timeColor[3],  test.timeColor[3],  ' ', test.timeColor[3], '|',  test.timeColor[4],  test.timeColor[4],  test.timeColor[4],  test.timeColor[4],  test.timeColor[4], '|'
            print '+---------------------+'
            print 'Readable Time\t\t', datetime.now().hour, datetime.now().minute
            print 'Non Readable Time\t', test.hour, test.minute
            print 'Fib Hours\t', test.fHour
            print 'Fib Minutes\t', test.fMinute
            '''
