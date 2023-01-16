# author = Lavanya Naresh
# created = Jan 16, 2023
# modified = Jan 16, 2023

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        merged = []
        idx, start, end = 0, 0, 1
        
        while idx < len(intervals) and intervals[idx][end] < newInterval[start]:
            
            merged.append(intervals[idx])
            idx += 1
            
        while idx < len(intervals) and intervals[idx][start] <= newInterval[end]:
            
            newInterval[start] = min(intervals[idx][start], newInterval[start])
            newInterval[end] = max(intervals[idx][end], newInterval[end])
            idx += 1
            
        merged.append(newInterval)
        
        while idx < len(intervals):
            
            merged.append(intervals[idx])
            idx += 1
            
        return merged
