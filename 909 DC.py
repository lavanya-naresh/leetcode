# author = Lavanya Naresh
# created = Jan 24, 2023
# modified = Jan 24, 2023


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        APPROACH:
        Keep track of visited squares using boolean list.
        Using queue iterate over possible moves that can be made.
        """
        n = len(board)
        m = n * n

        for row in range(n // 2):
            board[row], board[~row] = board[~row], board[row]
        for row in range(1, n, 2):
            board[row].reverse()

        # movement required from 1 to m so taking indices 0 to m with 0 as sentinel
        visited = {1}

        q = deque([1])
        moves = 1

        while q:
            for i in range(len(q)):
                u = q.popleft()
                k = min(m, u + 6)
                # possible next square value: u < next < k + 1
                for v in range(u + 1, k + 1):
                    # get the row and column of next square
                    row, col = divmod(v - 1, n)

                    if board[row][col] != -1:
                        v = board[row][col]

                    # if next square = final square, no further movement is required.
                    if v == m:
                        return moves

                    if v not in visited:
                        visited.add(v)
                        q.append(v)

            moves += 1

        # impossible to reach square n^2
        return -1
