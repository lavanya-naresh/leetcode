class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        GIVEN:
        --
        arr -> array of integers

        REQUIRED:
        --
        sum of all contiguous subarrays' min value [
        since answer may be v large, it is required to return answer % (10^9 + 7) ]

        CONSTRAINTS:
        --
        - 1 <= len(arr) <= 3 * 10^4
        - 1 <= arr[index] <= 3 * 10^4

        APPROACH:
        --
        1. Brute force: O(N^2)
        - An array of length N has N^2 subarrays -> This method will work upto a certain low value of N
        but after that threshold value it will result in TLE since we have to look for the min value in
        each subarray. How can we reduce the time complexity such that the solution has acceptable time
        complexity?

        2. Optimized approach:
        - To reduce the time complexity we could think of the number of times that a particular index will be the
        minimum value or the number of contiguous subarrays in which the value at a certain index will be the
        minimum value. To determine the number of subarrays where the integer at a given index i will be the min
        value in the subarray:
        - Each value will at least be the min value in 1 subarray since a subarray of length 1 can only have the
        solitary integer value in it as the min
        - So starting from the subarray of length 2 -> how can we determine if the value will be the min in a subarray
        of length 2? => This requires precise execution of the approach.

        - Assumption: all integers in arr are distinct

        Degree of freedom:
        -----------------
        The '|' indicates the index for which the degree is being determined.
        The left arrow indicates till which index towards the 0 th index it is possible for value at the pivot index to be
        the min value in the subarray and vice versa for the right pointing arrow. The array is:\n
        [3,1,2,4,5,8,6,7]
         |
         <-|----------->
             |--------->
               -------->
                 ------>
                   |
                   <-|->
                       |

        For example for value being 1, to the left we can take 2 subarrays [1], [3,1] for which 1 is the min value
        and to the right, we can take 7 subarrays. The number of possible combinations of subarrays generated using
        1 as the pivot index value = 2 * 7 = 14

        When the array has a value that can be the min in subarray sequences from both the left and the right side and
        its duplicate is present at such a position that it is possible to have an overlap in the counted sequences/ subarrays for
        which the value having duplicate(s) is the minimum. Example:
        [3,1,2,4,5,8,1,7]
         3,1,2,4,5,8,1
           1,2,4,5,8,1

        The issue of repetitive counting can be solved using tie breakers or in an arbitray way such as the value at the index closer to
        the end of the array being the 1 to contribute to being the min value of the subarray. This method would mean that when we are determining
        the DoF of the 1 closer to index 0 towards the right, then we will stop when we see the 1 closer to index N-1. However when counting towards
        the left from the 1 closer to index N-1, we can go past the 1 closer to 0th index. Then we can break the problem into 2 cases/ sub-problems:
        - What is the closest prev index that is smaller than this number?
        - What is the closest next index that is greater than or equal to this number?
        """
        total = 0
        stack = []
        arr.append(-inf)
        for index, num in enumerate(arr):
            print(f"FOR LOOP:\n\tindex, num: {index}, \t{num}")
            while stack and arr[stack[-1]] >= num:
                print("\tWHILE LOOP iteration")
                mid = stack.pop()
                print(f"\t\tstack after pop: {stack}")
                left = (stack[-1] if stack else -1) + 1
                right = index - 1
                total = (total + arr[mid] * (mid - left + 1) * (right - mid + 1)) % (
                    10**9 + 7
                )
                print(f"\t\tM, L, R, T: {mid}, {left}, {right}, {total}")
            stack.append(index)
            print(f"\tstack after append: {stack}")
        return total
