n, m = [int(i) for i in input().split()]
board = [['.'] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        board[i][j] = i * m + 1 + j

for row in board:
    print(*row)