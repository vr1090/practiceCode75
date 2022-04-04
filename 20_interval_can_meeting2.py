from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        count = 0
        maxCount =0
        start = []
        end = []

        for interval in intervals:
            start.append(interval.start)
            end.append( interval.end)

        start.sort()
        end.sort()

        s = 0
        e = 0

        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                s = s+ 1
                count = count + 1
            else:
                e = e + 1
                count = count -1 
            
            maxCount = max(maxCount, count)

        return maxCount