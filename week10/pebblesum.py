


def pebble(n, pebbles):
    dp = [[0 for _ in range(4)] for _ in range(n)]
    dp[0][0] = pebbles[0][0]
    dp[0][1] = pebbles[1][0]
    dp[0][2] = pebbles[2][0]
    dp[0][3] = pebbles[0][0] + pebbles[2][0]

    for i in range(1, n):
        for p in range(0, 4):
            if p == 0 :
                dp[i][p] = max(dp[i-1][1], dp[i-1][2]) + pebbles[0][i]
                continue
            if p == 1 :
                dp[i][p] = max(dp[i-1][0], dp[i-1][2], dp[i-1][3]) + pebbles[1][i]
                continue
            if p == 2 :
                dp[i][p] = max(dp[i-1][0], dp[i-1][1])+ pebbles[2][i]
                continue
            if p == 3 :
                dp[i][p] = dp[i-1][1] + pebbles[0][i] + pebbles[2][i]
    return max(dp[n-1][0], dp[n-1][1], dp[n-1][2], dp[n-1][3])


n = int(input())
p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))
pebbles = [p1, p2, p3]

print(pebble(n, pebbles))