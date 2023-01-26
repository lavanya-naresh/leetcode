# author = "Lavanya Naresh"
# created = "26-Jan-2023"
# modified = "26-Jan-2023"


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [inf] * n
        cost[src] = 0
        for _ in range(k + 1):
            new_cost = cost[:]
            for u, v, price in flights:
                new_cost[v] = min(new_cost[v], cost[u] + price)
            cost = new_cost
        return -1 if cost[dst] == inf else cost[dst]
