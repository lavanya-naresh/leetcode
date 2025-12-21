def paths_divisible_by_k(matrix, k):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[None] * (n + 1) for _ in range(m)]
    
    def dfs(i, j, k):
        if i == m - 1:
            return matrix[i][j] % k == 0
        
        if dp[i][j] != None:
            return dp[i][j]
        
        for dir in [[0, -1], [1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni, nj = i + dir[0], j + dir[1]
            if ni >= 0 and ni < m and nj >= 0 and nj < n:
                if dfs(ni, nj, k):
                    dp[i][j] = True
                    return dp[i][j]
        
        dp[i][j] = False
        return False
    
    res = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j, k):
                res += 1
    
    return res