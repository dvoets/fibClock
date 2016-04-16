#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 daan <daan@localhost>
#
# Distributed under terms of the MIT license.

"""
Documentation
"""

from fibSequence import fibMagic
from clock import clock
import random
from time import sleep
from datetime import datetime

if __name__ == "__main__":
    fSeq = fibMagic(5)
    time = clock(5, 5)
    hour = time.hour
    print('Hour', hour)
    while True:
        sleep(0.1)
        if time.timeChange():
            print('Current Time:', datetime.now())
            rFibMinute = random.choice(fSeq.fibDecomposed[time.minute/5])
            hour = time.hour
            print('Hour', hour)
            rFibHour = random.choice(fSeq.fibDecomposed[hour])
            print('Fib Hour for', hour, rFibHour)
            print('Fib Minure for', time.minute, rFibMinute)
