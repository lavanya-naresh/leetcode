# 3629. Minimum Jumps to Reach End via Prime Teleportation
# https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/description/
'''
Given that the starting point is index 0 and the target is the last index n - 1. The possible traversal steps are:
- next index i + 1
- previous index i - 1
- prime teleportation to any index j if nums[i] is a prime number and nums[j] % nums[i] == 0
Optimize for minimum number of jumps to reach the end.

Approach:
Shortest path problem that can be solved using BFS or Djikstra's algorithm.
Optimize for prime number by precomputing primes to the respective indices using sieve of Eratosthenes.
Track visited indices (nodes) to avoid cycles and redundant traversals.
'''
from typing import List
from collections import defaultdict, deque
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        N= len(nums)
        # edge case: single element
        if N == 1: return 0
        max_value = max(nums)
        smallest_prime_factors = list(range(max_value + 1))
        if max_value >= 0:
            smallest_prime_factors[0] = 0
        if max_value >= 1:
            smallest_prime_factors[1] = 1

        for index in range(2, max_value + 1):
            if smallest_prime_factors[index] == index:
                for multiple in range(index * index, max_value + 1, index):
                    if smallest_prime_factors[multiple] == multiple:
                        smallest_prime_factors[multiple] = index
        
        is_prime_sieve = [False] * (max_value + 1)

        for index in range(2, max_value + 1):
            if smallest_prime_factors[index] == index:
                is_prime_sieve[index] = True
        
        prime_index_map = defaultdict(list)
        for index in range(N):
            number = nums[index]
            temp = number
            unique_prime_factors = set()

            while temp > 1:
                prime_factor = smallest_prime_factors[temp]
                unique_prime_factors.add(prime_factor)
                while temp % prime_factor == 0:
                    temp //= prime_factor
                
            for prime_factor in unique_prime_factors:
                prime_index_map[prime_factor].append(index)
        
        q = deque([(0, 0)])
        visited = set([0])
        visited_primes = set()

        while q:
            current, jumps = q.popleft()

            if current == N - 1:
                return jumps

            forward_index = current + 1
            if forward_index < N and forward_index not in visited:
                visited.add(forward_index)
                q.append((forward_index, jumps + 1))
            
            backward_index = current - 1
            if backward_index >= 0 and backward_index not in visited:
                visited.add(backward_index)
                q.append((backward_index, jumps + 1))
            
            current_value = nums[current]

            if current_value <= max_value and current_value > 1 and is_prime_sieve[current_value]:
                prime_value = current_value
                
                if prime_value not in visited_primes:
                    visited_primes.add(prime_value)

                    for target_index in prime_index_map[prime_value]:
                        if target_index != current and target_index not in visited:
                            visited.add(target_index)
                            q.append((target_index, jumps + 1))
        return -1