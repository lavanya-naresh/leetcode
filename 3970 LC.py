# https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/description/
# 3970. Shortest Path With At Most K Consecutive Identical Characters

from collections import defaultdict
import heapq
from typing import List

'''
PROBLEM STATEMENT:
Given:
1. integer n representing the number of nodes in a directed weighted graph, numbered from 0 to n - 1.
2. This is represented by a 2D integer array edges where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with weight wi.
3. String labels of length n where labels[i] is the character assigned to node i.
4. integer k

REQUIRED:
minimum total edge weight of a path from node 0 to node n - 1 such that the concatenation of the labels of the nodes along the path contains at most k consecutive identical charactes. If no such path exists, return -1.

CONSTRAINTS:
    1. 1 <= n == labels.length <= 5 *10^4
    2. 0 <= edges.length <= 5 * 10^4
    3. 1 <= wi <= 10^4
    4. labels consists of lowercase English letters.
    5. 1 <= k <= 50

EXAMPLE:
1. Input: 
    n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1
    Output: 3
    Explanation:
        The optimal valid path from node 0 to node 2 is as follows:
        - Use edges[2] to reach from node 0 to node 2 with weight 3.
        The corresponding concatenation of the labels is "ab" which satisfies the condition of having at most 1 consecutive identical character.
2. Input:
    n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2
    Output: 2
    Explanation:
        Optimal path:
            - edges[0] = [0,1,1] traverse from 0 to 1 with weight 1
            - edges[1] = [1,2,1] traverse from 1 to 2 with weight 1
        The corresponding concatenation of the labels is "aab" which satisfies the condition of having at most 2 consecutive identical characters.
3. Input:
    n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2
    Output: -1
    Explanation:
        There is no valid path from node 0 to node 2 that meets the condition of at most 2 consecutive identical characters.

APPROACH:
    Keep track of the state of the path.
    Djikstra's algorithm

'''

class Solution:
    def shortestPath(self, N: int, edges: List[List[int]], labels: str, k: int) -> int:
        INF = 10 ** 20
        adj_list = defaultdict(list)
        for u, v, w in edges:
            adj_list[u].append((v, w))

        best = defaultdict(lambda: INF)
        def enqueue(node, distance, cons):
            heapq.heappush(h, (distance, cons, node))
            best[(node, cons)] = distance

        h = []
        enqueue(0, 0, 1)

        while len(h) > 0:
            d, c, current = heapq.heappop(h)

            if current == N - 1:
                return d

            if best[(current, c)] < d:
                continue

            for v, w in adj_list[current]:
                nd = d + w
                nc = 1
                if labels[current] == labels[v]:
                    nc = c + 1

                if nc <= k and nd < best[(v, nc)]:
                    enqueue(v, nd, nc)
        return -1