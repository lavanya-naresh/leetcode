# 1665. Minimum Initial Energy to Finish Tasks
# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/description
'''
Given an array tasks.
tasks[i] = [actual(i), minimum(i)]
actual(i) = the actual amount of energy you spend to finish the i th task.
minimum(i) = the minimum amount of energy you require to begin the i th task.
For example, if the task is [10, 12] and your current energy is 11, you cannot start this task. 
However, if your current energy is 13, you can complete this task, and your energy will be 3 after finishing it.
You can finish the tasks in any order you like.

Return the minimum initial amount of energy you will need to finish all the tasks.
Constraints:

    1 <= tasks.length <= 10^5
    1 <= actual(i) <= minimum(i) <= 10^4

Approach:
Sort the tasks in descending order of the difference between the minimum and actual energy required. This way, we prioritize tasks that have a larger gap between the minimum and actual energy, ensuring that we have enough energy to start those tasks first.
Iterate through the sorted tasks and keep track of the total energy spent and the minimum energy required to start the next task. Update the total energy spent and the minimum energy required accordingly.
'''
from typing import List


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0] - x[1], reverse=True)
        answer = 0
        for task in tasks:
            answer = max(answer + task[0], task[1])
        return answer