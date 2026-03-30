class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for n in range(9):
            if not self.row_validation(board, n):
                return False
            if not self.col_validation(board, n):
                return False

            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (n // 3) * 3 + i
                    col = (n % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True


    def row_validation(self,board: List[List[str]],row:int) -> bool:
        nums = ['1','2','3','4','5','6','7','8','9']
        for i in range(9):
            if board[row][i] == '.':
                continue 
            elif board[row][i] in nums:
                nums.remove(board[row][i])
            else:
                return False
        return True

    def col_validation(self, board: List[List[str]],col:int) -> bool:
        nums = ['1','2','3','4','5','6','7','8','9']
        for i in range(9):
            if board[i][col] == '.':
                continue 
            elif board[i][col] in nums:
                nums.remove(board[i][col])
            else:
                return False
        return True

    
