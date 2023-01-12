# author = Lavanya Naresh
# created = Jan 12, 2023
# modified = Jan 12, 2023

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [None] * n
        adj_list = collections.defaultdict(list)
        
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node, parent):
            current_freq = [0] * 26
            for child in adj_list[node]:
                if child != parent:
                    freq = dfs(child, node)
                    for index in range(26):
                        current_freq[index] += freq[index]

            current_freq[ord(labels[node]) - ord('a')] += 1
            ans[node] = current_freq[ord(labels[node]) - ord('a')]
            return current_freq
        
        dfs(0, -1)
        return ans
