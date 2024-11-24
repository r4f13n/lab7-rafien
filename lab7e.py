#!/usr/bin/env python3
# Student ID: 101775229

class Time:
    """Simple object type for time of the day.
        Data attributes: hour, minute, second
        Function attributes: __init__, __str__, __repr__,
                            time_to_sec, format_time,
                            change_time, sum_times, valid_time
    """
    def __init__(self, hour=0, minute=0, second=0):
        """Initialize a Time object with hour, minute, and second."""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        '''Return a string representation for the object self'''
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
    
    def __repr__(self):
        '''Return a string representation for the object self'''
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def format_time(self):
        """Return time object as a formatted string."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two time objects and return the sum as a new Time object."""
        self_sec = self.time_to_sec()
        t2_sec = t2.time_to_sec()
        return sec_to_time(self_sec + t2_sec)

    def change_time(self, seconds):
        """Change the time object by adding the given seconds."""
        time_seconds = self.time_to_sec()
        nt = sec_to_time(time_seconds + seconds)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second
        return None

    def time_to_sec(self):
        """Convert the time object to a single integer representing the 
        number of seconds since midnight."""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def valid_time(self):
        """Check for the validity of the time object attributes:
        0 <= hour < 24, 0 <= minute < 60, 0 <= second < 60."""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

def sec_to_time(seconds):
    """Convert a given number of seconds to a Time object."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

