from typing import List
import heapq

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        result = 0
        previous = [0] * cols

        for row in range(rows):
            heap = []
            for col in range(cols):
                previous[col] += -previous[col] if matrix[row][col] == 0 else 1
                if previous[col]:
                    heap.append(previous[col])
            
            heapq.heapify(heap)
            while heap:
                result = max(result, len(heap) * heap[0])
                heapq.heappop(heap)
        return result