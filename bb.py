from datetime import *

class CallCounter:
    def __init__(self):
        self.counter = 0
    def __call__(self):
        self.counter +=1
    def __getitem__(self):
        return self.counter
a = CallCounter()
a()
print(a.__getitem__())




class DateRange:
    def __init__(self, datestart, dateend):
        sy,sm,sd = map(int, datestart.split('-'))
        ey,em,ed = map(int, dateend.split('-'))
        self.start = date(sy, sm, sd)
        self.end = date(ey,em,ed)
        self.daterange = [self.start.isoformat()]
        dt = self.start
        while dt != self.end:
            if dt.day < 32 and dt.month < 13:
                if dt.day == 31 and dt.month<12:
                    dt = date(dt.year, dt.month+1, 1)
                elif dt.day == 31 and dt.month == 12:
                    dt = date(dt.year+1, 1, 1)
                else:
                    dt = date(dt.year, dt.month, dt.day+1)
            self.daterange.append(dt.isoformat())
    def __iter__(self):
        return iter(self.daterange)
        
a = DateRange('1999-12-03', '2000-02-10')
for i in a:
    print(i)