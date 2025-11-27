import sys

input = sys.stdin.readline

n, k = map(int, input().split())

graph = [[] for i in range(n + 1)]

for i in range(k):
    u, v, w = list(map(int, input().split()))
    graph[u].append((v, w))

r, t = map(int, input().split())

def Dijkstra(G, r):
    distances = [float('inf')] * (n + 1)
    visited = [False] * (n + 1)
    path = [0] * (n + 1)
    distances[r] = 0

    for _ in range(n):
        min_val = float('inf')
        u = -1

        for i in range(1, n + 1):
            if not visited[i] and distances[i] < min_val:
                min_val = distances[i]
                u = i

        # 더 이상 갈 곳이 없거나 연결되지 않음
        if u == -1:
            break

        # 2. S에 추가 (방문 처리)
        visited[u] = True

        # 3. Relaxation
        for v, w in G[u]:
            # if v ∈ V-S and ...
            # 여기서 visited[v]를 체크해도 되지만,
            # 이미 방문한 노드는 거리가 더 줄어들지 않으므로 거리 비교만 해도 무방
            if not visited[v] and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                path[v] = u

    return distances, path[1:]

d, p = Dijkstra(graph, r)

for i in p:
    print(i, end=" ")

if d[t] == float('inf'):
    print("Impossible")
else:
    print(d[t])


