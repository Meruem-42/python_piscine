import math

class TinyStatistician() :
    def __init__(self) :
        self.array = None

    def mean(self, x) :
        if len(x) == 0 :
            return None
        sum = x[0]
        for elem in x[1::] :
            sum += elem
        return(sum / len(x))

    def median(self, x) :
        if len(x) == 0 :
            return None
        x.sort()
        return x[round(len(x) / 2 - 1)]

    def quartile(self, x) :
        if len(x) == 0 :
            return None
        x.sort()
        lst_len = len(x)
        return [x[math.floor((lst_len - 1) * 0.25)], x[math.floor((lst_len - 1) * 0.75)]]

    def var(self, x) :
        if len(x) == 0 :
            return None
        lst_len = len(x)
        mean = self.mean(x)
        var = 0
        for elem in x :
            var += (elem - mean)**2 / lst_len
        return var

    def std(self, x) :
        if len(x) == 0 :
            return None
        return math.sqrt(self.var(x))

