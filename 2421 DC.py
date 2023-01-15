# author = Lavanya Naresh
# created = Jan 15, 2023
# modified = Jan 15, 2023

class UnionFind:
    def __init__(self):
        self._parent = {}
        self._size = {}
    
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self._size[a] < self._size[b]:
            a, b = b, a
        self._parent[b] = a
        self._size[a] += self._size[b]
        return True
    
    def find(self, x):
        if x not in self._parent:
            self._parent[x] = x
            self._size[x] = x
        while self._parent[x] != x:
            self._parent[x] = self._parent[self._parent[x]]
            x = self._parent[x]
        return x
    
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        groups = defaultdict(list)
        for index, val in enumerate(vals):
            groups[val].append(index)
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        uf = UnionFind()
        good_paths = 0
        for val in sorted(groups):
            for u in groups[val]:
                for v in graph[u]:
                    if vals[v] <= vals[u]:
                        uf.union(u, v)
            counts = defaultdict(int)
            for u in groups[val]:
                counts[uf.find(u)] += 1
            for count in counts.values():
                good_paths += count * (count + 1) // 2
        
        return good_paths
