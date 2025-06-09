class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        if n < 10:
            return k
        N = len(str(n))

        def solve(pos, acc, k):
            if k == 1:
                return acc
            k -= 1
            if pos == N - 1 and k < 10:
                return acc * 10 + k - 1
            for i in range(10):
                total = 0
                for size in range(1, N - pos + 1):
                    base = (acc * pow(10, size)) + i * pow(10, size - 1)
                    if base > n:
                        continue
                    if str(acc * 10 + i) == str(n)[:pos+1] and len(str(base)) == N:
                        total += int(str(n)[(pos+1):]) + 1
                    else:
                        total += pow(10, size - 1)
                if total >= k:
                    return solve(pos + 1, acc*10 + i, k)
                else:
                    k -= total

        first = int(str(n)[0])
        for i in range(1, 10):
            total = 0
            for size in range(1, N + 1):
                base = i * pow(10, size - 1)
                if base > n:
                    continue
                total += int(str(n)[1:]) + 1 if i == first and size == N else pow(10, size - 1)
            if total >= k:
                return solve(1, i, k)
            else:
                k -= total
        return -1