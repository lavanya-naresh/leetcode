# author = Lavanya Naresh
# created = Jan 25, 2023
# modified = Jan 25, 2023


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        """
        NOTE:
        Since there is at most 1 outgoing edge from each node,
        there is no requirement to keep track of visited nodes.
        """
        def dfs(u):
            stack = [u]
            dist = [inf] * len(edges)
            dist[u] = 0
            while stack:
                u = stack.pop()
                v = edges[u]
                if v != -1 and dist[v] == inf:
                    stack.append(v)
                    dist[v] = dist[u] + 1
            return dist

        res = [max(a, b) for (a, b) in zip(dfs(node1), dfs(node2))]
        return res.index(min(res)) if min(res) != inf else -1
