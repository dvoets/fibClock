import collections


class fSeq:
    def __init__(self, fNumbers):
        self.fNumbers = fNumbers
        self.seq = self.fSequence()
        self.fDecom = self.fDecomposition()

    def fSequence(self):
        if self.fNumbers == 1:
            fSeq = [1]
        else:
            fSeq = [1, 1]
            if self.fNumbers > 2:
                for i in range(2, self.fNumbers):
                    fSeq.append(fSeq[i-2]+fSeq[i-1])
        return fSeq

    def fDecomposition(self):
        d = {}
        for i in range(2**self.fNumbers):
            fmt = '{0:0' + str(self.fNumbers) + 'b}'
            binToSubset = map(int, list(fmt.format(i)))
            property_asel = [val for is_good, val in zip(binToSubset, self.seq) if is_good]
            d.setdefault(sum(property_asel), []).append(binToSubset)
        return d
    def toon(self):
        print self.seq

if __name__ == '__main__':
    test = fSeq(5)
    for i in range(12):
        print 'i', test.fDecom[i]
