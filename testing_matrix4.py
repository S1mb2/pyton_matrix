n, m = [int(i) for i in input().split()]

matrix = [[1 for _ in range(m)] for _ in range(n)]
count = 0

for q in range(n+m-1):
    for i in range(n):
        for j in range(m):
            if i+j == q:
                count += 1
                matrix[i][j] = count
for row in matrix:
    print(*row)