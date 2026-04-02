class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [[[] for _ in range(3)] for _ in range(3)]
        boxesSet = [[set() for _ in range(3)] for _ in range(3)]
        rowIndex = 0
        colIndex = 0
        for rowIndex in range(len(board)):
            for colIndex in range(len(board[0])):
                if(board[rowIndex][colIndex] == '.'):
                    continue
                rowBoxIndex = rowIndex //3
                colBoxIndex = colIndex // 3
                boxes[rowBoxIndex][colBoxIndex].append(board[rowIndex][colIndex])
                boxesSet[rowBoxIndex][colBoxIndex].add(board[rowIndex][colIndex])
        for boxIndexRow in range(len(boxes)):
            for boxIndexCol in range(len(boxes[0])):
                if len(boxes[boxIndexRow][boxIndexCol]) != len(boxesSet[boxIndexRow][boxIndexCol]):
                    print("Box failure!", boxes[boxIndexRow][boxIndexCol], boxesSet[boxIndexRow][boxIndexCol])
                    return False

        colSet = [set() for _ in range(10)]
        for rowIndex in range(len(board)):
            evalBoard = []
            evalSetBoard = set()
            for col in board[rowIndex]:
                if(col == '.'):
                    continue
                evalBoard.append(col)
                evalSetBoard.add(col)

            if len(evalBoard) != len(evalSetBoard):
                print("row Failure", evalBoard, set(board[rowIndex]))
                return False

            for k in range(len(board[0])):
                if(
                   board[rowIndex][k] != '.' 
                ):
                    size = len(colSet[k])
                    colSet[k].add(board[rowIndex][k])
                    if size == len(colSet[k]):
                        print("col failure!")
                        return False

        return True
        