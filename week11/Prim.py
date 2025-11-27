n, m = list(map(int, input().split()))
graph = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, w = list(map(int, input().split()))
    if x == y :
        continue
    graph[x-1][y-1] = w
    graph[y-1][x-1] = w


def Prim(graph, n):
    Q = []#아직 포함되지 않은 정점들의 집합. 처음에는 모든 정점이 들어 있음.
    d = []#값을 저장하는 리스트 해당 정점까지 연결할때 드는 최소 비용
    tree = [] #최소 신장 트리에 포함된 간선을 저장하는 리스트
    weight = 0
    for i in range(n):
        Q.append(i)
        d.append(float('inf'))
        tree.append(None)
    d[0] = 0
    while Q:
        u = EXTRACT_MIN(Q, d)
        Q.remove(u)
        print(u+1, end=' ')
        weight += d[u]
        for v in range(n):
            if graph[u][v] != 0 and v in Q and graph[u][v] < d[v]:
                d[v] = graph[u][v]
                tree[v] = u
    return weight
def EXTRACT_MIN(Q, d):
    min_index = Q[0]
    for i in Q:
        if d[i] < d[min_index]:
            min_index = i
    return min_index


w = Prim(graph, n)
print(w)
