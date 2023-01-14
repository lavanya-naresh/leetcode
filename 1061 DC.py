# author = Lavanya Naresh
# created = Jan 10, 2023
# modified = Jan 10, 2023

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        p = {c:c for c in 'abcdefghijklmnopqrstuvwxyz'}
        
        def find(u):
            if p[u] == u:
                return u
            p[u] = find(p[u])
            return p[u]
        
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu != pv:
                if pv < pu:
                    p[pu] = pv
                else:
                    p[pv] = pu
        
        for c1, c2 in zip(s1, s2):
            union(c1, c2)
            
        ans = ''
        for c in baseStr:
            ans += find(c)
        
        return ans
