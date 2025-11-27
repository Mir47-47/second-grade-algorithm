n = int(input())
m = int(input())
graph = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(m):
    x, y = list(map(int, input().split()))
    if x == y :
        continue
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

def DFS(start, visited):
    if not visited[start]:
        visited[start] = True
        print(start+1, end=' ')
    else :
        return visited
    for i in range(0, n):
        if graph[start][i] == 1 and not visited[i]:
            visited = DFS(i, visited)
    return visited

visited = [False for _ in range(n)]

k = int(input())
visited = DFS(k-1, visited)
for i in range(0, n):
    visited = DFS(i, visited)