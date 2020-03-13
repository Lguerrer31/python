DAY = 1440

class Clock(object):
    def __init__(self, hour, minute):
        self.minutes = ((hour * 60) + minute) % DAY

    def __repr__(self):
        return '{}:{}'.format(
                str(self.minutes // 60).zfill(2),
                str(self.minutes % 60).zfill(2)
            )

    def __eq__(self, other):
        return self.minutes == other.minutes

    def __add__(self, minutes):
        return Clock(0, self.minutes + minutes)

    def __sub__(self, minutes):
        return Clock(0, self.minutes - minutes)
