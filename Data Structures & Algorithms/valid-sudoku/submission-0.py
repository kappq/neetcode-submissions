class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRows(board) and self.checkCols(board) and self.checkBoxes(board)

    def checkRows(self, board: List[List[str]]) -> bool:
        for row in board:
            for num in range(1, 10):
                if row.count(str(num)) > 1:
                    return False
        return True

    def checkCols(self, board: List[List[str]]) -> bool:
        cols = [[board[i][j] for i in range(9)] for j in range(9)]
        return self.checkRows(cols)

    def checkBoxes(self, board: List[List[str]]) -> bool:
        boxes = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                boxes[i // 3 * 3 + j // 3].append(board[i][j])
        return self.checkRows(boxes)