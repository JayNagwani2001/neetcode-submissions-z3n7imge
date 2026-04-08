class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        grid = [[[] for _ in range(3)] for _ in range(3)]
        print(grid)
        for i in range(9):
            # print(rows)
            # print(grid)
            for j in range(9):

                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i]:
                    # print('row')
                    return False
                if board[i][j] in cols[j]:
                    # print('col')
                    return False
                if board[i][j] in grid[i//3][j//3]:
                    # print('grid')
                    return False
                rows[i].append(board[i][j])
                cols[j].append(board[i][j])
                grid[i//3][j//3].append(board[i][j])
                print(grid)
                print(grid[i//3][j//3])

           
        
        return True
        

