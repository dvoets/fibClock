#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 daan <daan@localhost.localdomain>
#
# Distributed under terms of the MIT license.

"""
Documentation
"""

from datetime import datetime, timedelta
import time


class clock:
    """class that will check if the time has changed based on:
            - unit = divide minutes in buckets of units
            - offset = starts offset seconds before"""
    def __init__(self, unit, offset):
        self.unit, self.offset = unit, offset
        self.prevHour = self.tOffset().hour
        self.prevMinute = self.tOffset().minute - self.tOffset().minute % 5
        self.hour = self.prevHour
        self.minute = self.prevMinute
        print('Start Time', self.prevHour, ':', self.prevMinute)
        print('Current Time', datetime.now())

    def tOffset(self):
        """adds offset seconds to time"""
        now = datetime.now() + timedelta(seconds=self.offset)
        return now

    def timeChange(self):
        """function returns True if time has changed otherwise False"""
        now = self.tOffset()
        self.hour = now.hour
        self.minute = now.minute - now.minute % 5
        if self.minute == self.prevMinute:
            return False
        else:
            self.prevHour = self.hour
            self.prevMinute = self.minute
            return True


if __name__ == "__main__":
    c = clock(5, 6)
    while True:
        time.sleep(0.1)
        if c.timeChange():
            print('New Time', c.hour, ':', c.minute)
            print('Current Time', datetime.now())
