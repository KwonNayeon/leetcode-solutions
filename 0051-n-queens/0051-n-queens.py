class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        board = [["." for _ in range(n)] for _ in range(n)]

        def is_safe(row, col):
            # 같은 열
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # 왼쪽 위 대각선
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # 오른쪽 위 대각선
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            
            return True
        
        def backtrack(row):
            # 만약 모든 행 다 놨으면
            if row == n:
                # 보드를 문자열로 변환하여 추가
                result = ["".join(row) for row in board]
                solutions.append(result)
                return

            for col in range(n):
                    if is_safe(row, col):
                        board[row][col] = 'Q'
                        # 다음 행 호출
                        backtrack(row + 1)
                        board[row][col] = "."
        
        backtrack(0)
        return solutions
