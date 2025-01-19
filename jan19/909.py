

from collections import deque
from types import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()
        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 -c
            return [r, c]

        q = deque()

        q.append([1, 0])
        visited = set()

        while q:
            square, moves = q.popleft()

            for i in range(1, 7):
                nextSquare = square + i
                nr, nc = intToPos(nextSquare)
                if board[nr][nc] != -1:
                    nextSquare = board[nr][nc]
                if nextSquare == length * length:
                    return moves + 1
                if nextSquare not in visited:
                    visited.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        return -1

# Time Complexity: O(n^2)

# Space Complexity: O(n^2)