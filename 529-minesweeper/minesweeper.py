class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        ci, cj = click
        def dfs(ci, cj, board):
            m, n = len(board), len(board[0])
            if board[ci][cj] != 'E':
                return
            
            n_mines = 0
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                ni, nj = ci+i, cj+j
                if 0 <= ni < m and 0 <= nj < n and board[ci+i][cj+j] == 'M':
                    n_mines += 1
            
            if n_mines != 0:
                board[ci][cj] = str(n_mines)
                return
            
            board[ci][cj] = 'B'
            # Revealed Blank Square: Keep DFS
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                ni, nj = ci+i, cj+j
                if 0 <= ni < m and 0 <= nj < n:
                    dfs(ni, nj, board)
            
            return
                
        
        if board[ci][cj] == 'M':
            board[ci][cj] = 'X'
        elif board[ci][cj] == 'E':
            n_mines = 0
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                ni, nj = ci+i, cj+j
                if 0 <= ni < m and 0 <= nj < n and board[ci+i][cj+j] == 'M':
                    n_mines += 1
            
            if n_mines == 0:
                dfs(ci, cj, board)
                board[ci][cj] = 'B'
            else:
                board[ci][cj] = str(n_mines)
            
        
        return board