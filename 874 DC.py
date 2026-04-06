from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions: [right, up, left, down]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initialize position and direction
        x, y = 0, 0
        direction_index = 0
        
        # Convert obstacles to a set for O(1) lookups
        obstacle_set = set(map(tuple, obstacles))
        
        # Variable to keep track of the maximum distance from the origin
        max_distance = 0
        
        for command in commands:
            if command == -2:  # Turn left
                direction_index = (direction_index - 1) % 4
            elif command == -1:  # Turn right
                direction_index = (direction_index + 1) % 4
            else:
                dx, dy = directions[direction_index]
                for _ in range(command):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) not in obstacle_set:
                        x, y = nx, ny
                        max_distance = max(max_distance, x**2 + y**2)
        
        return max_distance

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    commands = [4, -1, 3]
    obstacles = []
    print(solution.robotSim(commands, obstacles))  # Output: 25