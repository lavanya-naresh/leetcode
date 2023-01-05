# author = Lavanya Naresh
# created = Jan 5, 2023
# modified = Jan 5, 2023

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x: x[1])
        end = points[0][1]
        result = 1
        for i in range(1, len(points)):
            current = points[i]
            if current[0] <= end:
                continue
            end = current[1]
            result += 1
        return result
