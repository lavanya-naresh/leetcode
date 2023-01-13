# author = Lavanya Naresh
# created = Jan 13, 2023
# modified = Jan 13, 2023

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adj_list = collections.defaultdict(list)
        N = len(s)

        for u, p in enumerate(parent):
            # skip sentinel to root edge as not applicable for our use case
            if p == -1: continue
            # if the character attached to the nodes are the same, do not add edge to adjacency list
            if s[u] == s[p]: continue

            adj_list[u].append(p)
            adj_list[p].append(u)
        # store best result obtained in a nonlocal variable and track visited nodes using a boolean list
        best = 0
        visited = [False] * N
        # depth of the path rooted at node=node with parent=parent
        def solver(node, parent):
            visited[node] = True
            longest = []
            for child in adj_list[node]:
                if child != parent:
                    longest.append(solver(node=child, parent=node))
                    
                    if len(longest) >= 3 and  longest[2] > longest[1]:
                        longest[1], longest[2] = longest[2], longest[1]
                    if len(longest) >= 2 and longest[1] > longest[0]:
                        longest[0], longest[1] = longest[1], longest[0]
                    
                    if len(longest) >= 3:
                        longest.pop()
            nonlocal best
            best = max(best, sum(longest) + 1)            
            return max(longest, default=0) + 1
        
        for index in range(N):
            if not visited[index]:
                solver(index, -1)
        return best
