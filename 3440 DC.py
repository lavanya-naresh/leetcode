# 3440. Reschedule Meetings for Maximum Free Time II
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        blocks = [(0, 0)] + list(zip(startTime, endTime)) + [(eventTime, eventTime)]
        gaps = [0] * len(blocks)
        for i in range(1, len(blocks) - 1):
            gaps[i] = max(gaps[i - 1], blocks[i][0] - blocks[i - 1][1])
        rgaps = [0] * len(blocks)
        for i in reversed(range(1, len(blocks) - 1)):
            rgaps[i] = max(rgaps[i + 1], blocks[i + 1][0] - blocks[i][1])
        max_free_time = 0
        for i in range(1, len(blocks) - 1):
            block_width = blocks[i][1] - blocks[i][0]
            gap_width = blocks[i + 1][0] - blocks[i - 1][1]
            max_gap = max(gaps[i - 1], rgaps[i + 1])
            max_free_time = max(max_free_time, gap_width - block_width)
            if max_gap >= block_width:
                max_free_time = max(max_free_time, gap_width)
        return max_free_time