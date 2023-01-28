# author = Lavanya Naresh
# created = Jan 28, 2023
# modified = Jan 28, 2023


class SummaryRanges:

    def __init__(self):
        self._nums = set()


    def addNum(self, value: int) -> None:
        self._nums.add(value)
        

    def getIntervals(self) -> List[List[int]]:
        intervals = []
        for num in sorted(self._nums):
            if not intervals or intervals[-1][1] < (num - 1):
                intervals.append([num, num])
            else:
                intervals[-1][1] = num
        return intervals
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
