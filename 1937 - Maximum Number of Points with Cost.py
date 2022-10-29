# 1937 - Maximum Number of Points with Cost

class Solution(object):
    def maxPoints(self, points):
    	m, n = len(points), len(points[0])
    	dp = points[0]
    	#  iterate from row 1 to last row ie. row (m-1)
    	for row in range(1, m):
    		prefix = [0] * n
    		prefix[0] = dp[0]
    		# iterate over columns 1 to (n-1)
    		for col in range(1, n):
    			prefix[col] = max(prefix[col - 1], dp[col] + col)
    		suffix = [0] * n
    		suffix[-1] = dp[-1] - (n - 1)

    		for col in reversed(range(n - 1)):
    			suffix[col] = max(suffix[col + 1], dp[col] - col)
    		recent = [0] * n
    		for col in range(n):
    			recent[col] = max(prefix[col] - col, suffix[col] + col) + points[row][col]
    		dp = recent
    	return max(dp)