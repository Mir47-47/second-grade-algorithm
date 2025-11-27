import sys
def rMatrixChain(p, n):
    m = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(1, n-1):
        for i in range(1, n - r):
            j = i + r
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q

    return m[1][n-1]




n = int(input())
mat = [tuple(map(int, input().split())) for _ in range(n)]

p = [mat[0][0]] + [mat[i][1] for i in range(n)]

print(rMatrixChain(p, n+1))

