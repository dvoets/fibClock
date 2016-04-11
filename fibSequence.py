#! /usr/bin/env python3
# -*- coding: utf-8 -*-


class fibMagic:
    """Class the can calcutate:
            - fibonacci squence
            - decompose an integer into the sum of fibonacci numbers"""
    def __init__(self, lFibSeq):
        self.lFibSeq = lFibSeq
        self.fibSequence = self.fibSeq()
        self.fibDecomposed = self.fibDecom()

    def fibSeq(self):
        """Fibonnaci sequence"""
        a, b = 0, 1
        fSeq = []
        for i in range(self.lFibSeq):
            a, b = b, a + b
            fSeq.append(a)
        return fSeq

    def fibDecom(self):
        """Decomposes intiger in sum of fibonacci numbers"""
        seq = {}
        for i in range(2**self.lFibSeq):
            fmt = '{0:0' + str(self.lFibSeq) + 'b}'
            sqnc = [int(a)*b for a, b in zip(fmt.format(i), self.fibSequence)]
            sumSequence = sum(sqnc)
            if sumSequence in seq.keys():
                seq[sumSequence].append(sqnc)
            else:
                seq[sumSequence] = [sqnc]
        return seq


if __name__ == '__main__':
    t = fibMagic(5)
    for i in t.fibDecomposed.keys():
        for j in t.fibDecomposed[i]:
            print('Sum: ', i,  'of: ', j)
