# 1865. Finding Pairs With a Certain Sum
from collections import Counter
from typing import List
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        previous = self.nums2[index]
        self.nums2[index] += val
        self.freq[previous] -= 1
        self.freq[previous + val] += 1

    def count(self, tot: int) -> int:
        result = 0
        for number in self.nums1:
            result += self.freq[tot - number]
        return result
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)