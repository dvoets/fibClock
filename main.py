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


if __name__ == "__main__":
    fSeq = fibMagic(5)
    time = clock(5, 5)
    if True:
        rFibMinute = random.choice(fSeq.fibDecomposed[time.minute/5])
        print(rFibMinute)
        hour = time.hour

        if hour > 12:
            hour -= 12
        rFibHour = random.choice(fSeq.fibDecomposed[hour])
        print('Fib Hour for', hour, rFibHour)
        print('Fib Minure for', time.minute, rFibMinute)
