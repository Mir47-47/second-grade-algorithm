n = int(input())
m = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y = list(map(int, input().split()))
    if x == y :
        continue
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1
def BFS(start, visited, graph, n):

    visited[start] = True
    print(start+1, end=' ')
    queue = []
    for x in range(0, n):
        if graph[start][x] == 1 and not visited[x]:
            queue.append(x)
            visited[x] = True
    while queue:
        start = queue.pop(0)
        print(start+1, end=' ')
        for x in range(0, n):
            if graph[start][x] == 1 and not visited[x]:
                queue.append(x)
                visited[x] = True
    return visited

visited = [False for _ in range(n)]
k = int(input())
visited = BFS(k-1, visited, graph, n)
