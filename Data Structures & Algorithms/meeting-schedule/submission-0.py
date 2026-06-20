"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        Count= len(intervals)
        for i in range(Count-1):
            if intervals[i].end >= intervals[i+1].end:
                return False
        return True

            

