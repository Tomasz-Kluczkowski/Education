class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """Create a MyTime object initialized to hrs, mins, secs.
        The vlue of mins and secs can be outside the range 0-59,
        but the resulting MyTime object will be normalized"""
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs // 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def to_seconds(self) -> int:
        """Return the number of seconds represented by this instance"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self.hours, self.minutes, self.seconds)

    def increment(self, seconds):
        self.seconds += seconds

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1

    def add_time(self, t2):

        secs = self.to_seconds() + t2.to_seconds()
        return MyTime(0, 0, secs)

    def after(self, time2):
        """Return True if I am strictly greater than time2
        :type time2: MyTime
        """
        return self.to_seconds() > time2.to_seconds()

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        return MyTime(0, 0, self.to_seconds() - other.to_seconds())


current_time = MyTime(9, 14, 30)
bread_time = MyTime(3, 35, 0)
done_time = current_time.add_time(bread_time)


time1 = MyTime(11,59,30)
print(time1)

t1 = MyTime(1, 15, 42)
t2 = MyTime(3, 50, 30)
t3 = t1 + t2
print(t3)

t4 = t2 - t1
print(t4)