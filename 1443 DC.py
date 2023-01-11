class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        times = [0] * n
        stack = [(0, -1, True)]
        while stack:
            u, p, is_new = stack.pop()
            if is_new:
                stack.append((u, p, False))
                for v in graph[u]:
                    if v == p:
                        continue
                    stack.append((v, u, True))
            else:
                for v in graph[u]:
                    if v == p:
                        continue
                    if hasApple[v] or times[v] > 0:
                        times[u] += 2 + times[v]
        return times[0]
