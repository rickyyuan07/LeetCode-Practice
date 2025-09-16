class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[0] * n for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        n = self.n
        h, v, d1, d2 = player, player, player, player
        for i in range(n):
            if self.board[row][i] != player:
                h = 0
            if self.board[i][col] != player:
                v = 0
            if row != col or self.board[i][i] != player:
                d1 = 0
            if row + col != n-1 or self.board[i][n-i-1] != player:
                d2 = 0
        
        if h or v or d1 or d2:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)