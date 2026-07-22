# 1081. Smallest Subsequence of Distinct Characters
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description

'''
GIVEN:
string s

REQUIRED:
Return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

CONSTRAINTS:
1 <= s.length <= 1000
s consists of lowercase English letters.
'''

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        N = len(s)
        alpha = list(sorted(set(s)))
        C = len(alpha)

        done = set()
        ans = []
        last = -1
        for k in range(C):
            found_index = False
            # can alpha[i] be used next
            for i in range(C):
                if alpha[i] in done:
                    continue

                found = False
                rest = set()
                first = None

                for j in range(last + 1, N):
                    if not found and alpha[i] == s[j]:
                        first = j
                        found = True
                        continue

                    if found:
                        if s[j] not in done and s[j] != alpha[i]:
                            rest.add(s[j])

                if len(rest) != C - k - 1:
                    continue
                
                ans.append(alpha[i])
                last = first
                done.add(alpha[i])
                break
        return "".join(ans)