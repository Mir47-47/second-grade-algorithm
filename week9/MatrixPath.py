n, m = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(m+1)]

for i in range(1,m+1):
    row = list(map(int, input().split()))
    for j in range(1,n+1):
        matrix[i][j] = row[j-1]

dp = [[0] * (n+1) for _ in range(m+1)]
for i in range(2, m+1):
    dp[i][0] = 99999
for j in range(2, n+1):
    dp[0][j] = 99999
dp[1][1] = matrix[1][1]
for i in range(1, m+1):
    for j in range(1, n+1):
        if i == 1 and j == 1:
            continue
        dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i][j-1])


print(dp[m][n])