# Multiplication table

n, m = int(input()), int(input())

mult = [[str(i*j).ljust(3) for i in range(m)] for j in range(n)]

[print(*i) for i in mult]