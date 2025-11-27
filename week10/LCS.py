
def LCSdp(X, Y):

    m = len(X)
    n = len(Y)

    C = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    return C[m][n]

x = input()
y = input()

print(LCSdp(x, y))