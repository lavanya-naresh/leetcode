# author = Lavanya Naresh
# created = Jan 8, 2023
# modified = Jan 8, 2023

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        INF = 10 ** 10
        
        def max_points_on_line_with_ith_point(i):
            
            def slope_coprime(x1, y1, x2, y2):
                
                dx, dy = x1 - x2, y1 - y2
                if dx == 0:
                    return (0, 0)
                elif dy == 0:
                    return (INF, INF)
                elif dx < 0:
                    dx, dy = -dx, -dy
                gcd = math.gcd(dx, dy)
                slope = (dx / gcd, dy / gcd)
                
                return slope
            
            def add_line(i, j, count, duplicates):
                
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]
                
                if x1 == x2 and y1 == y2:
                    duplicates += 1
                elif y1 == y2:
                    nonlocal horizontal_lines
                    horizontal_lines += 1
                    count = max(horizontal_lines, count)
                else:
                    slope = slope_coprime(x1, y1, x2, y2)
                    lines[slope] = lines.get(slope, 1) + 1
                    count = max(lines[slope],count)
                
                return count, duplicates
            
            lines, horizontal_lines = {}, 1
            count, duplicates = 1, 0
            for j in range(i + 1, N):
                count, duplicates = add_line(i, j, count, duplicates)
            return count + duplicates

        N = len(points)
        if N < 3: return N
        result = 1

        for i in range(N - 1):
            result = max(max_points_on_line_with_ith_point(i), result)

        return result
