# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/
# 1385. Find the Distance Value Between Two Arrays

'''
Given:
int[] arr1, arr2
int d

Return the distance value between the two arrays.
The distance value is defined as the number of elements arr1[i] such that
there is not any element arr2[j] where 
| arr1[i] - arr2[j] | <= d

Constraints:
1. 1 <= arr1.length, arr2.length <= 500
2. -1000 <= arr1[i], arr2[j] <= 1000
3. 0 <= d <= 100
Examples:
1.  Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
    Output: 2
2.  Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
    Output: 2
3.  Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
    Output: 1

Approach:
Iterate through each element in arr1 and check if the absolute diff between that and each element in arr2 > d.
If true for all elements in arr2, increment the result counter.
'''

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        result = 0
        for i in arr1:
            if all(abs(i - j) > d for j in arr2):
                result += 1
        return result