from unit_testing import test

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

        time = MyTime(0, 0, self.to_seconds() + seconds)
        self.hours = time.hours
        self.minutes = time.minutes
        self.seconds = time.seconds


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

    def between(self, t1, t2):
        """Returns true if invoking object is between times t1 and t2
        :type t1: MyTime
        :type t2: MyTime
        """

        return t1.to_seconds() <= self.to_seconds() < t2.to_seconds()

    def __gt__(self, other):
        """Allows to compare two MyTime objects"""
        return self.to_seconds() > other.to_seconds()



t1 = MyTime(10,50,30)
t2 = MyTime(14,55,23)
t3 = MyTime(11,12,12)

print(t3.between(t1, t2))
print(t2 > t1)

t1.increment(10)
print(t1)

t1.increment(-20)
print(t1.seconds == 20)
print(t1)

t1.increment(-30)
print(t1)
print(str(t1) == "10:49:50")

t1.increment(3600)
print(t1)
print(str(t1) == "11:49:50")

