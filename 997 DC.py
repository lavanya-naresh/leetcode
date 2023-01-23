# author = Lavanya Naresh
# created = Jan 24, 2023
# modified = Jan 24, 2023


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # edge case
        if n == 1:
            return 1
        
        # count: key = person, value = person trusted by value number of people
        # Town judge should appear as key with value (n - 1).
        # rev_count: bool dict to track if key = person trusts any person.
        # Town judge shouldn't appear in this dict as key.
        count = collections.Counter()
        rev_count = {}
        
        for x in trust:
            if x[1] in count:
                count[x[1]] += 1
            else:
                count[x[1]] = 1
            
            rev_count[x[0]] = True
        
        for x in count:
            # check required conditions as mentioned above
            if x not in rev_count and count[x] == n - 1:
                return x
        # Impossible to have a town judge
        return -1
