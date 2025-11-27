
n, k = list(map(int, input().split()))

parent = [i for i in range(n + 1)]

edge = []
for i in range(k):
    t = list(map(int, input().split()))
    edge.append(t)

edge.sort(key=lambda x:x[2])


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    roota = find(x)
    rootb = find(y)
    if roota != rootb:
        parent[rootb] = roota
        return True
    return False
#
#
# def Kruskal(graph_set, edge):
#     T= []
#     weight = 0
#     while len(T) < n-1:
#         w, u, v = edge.pop(0)
#         if find(u) != find(v):
#             union(u, v)
#             weight += w
#     return weight

def MST_KRUSKAL(G, w):
    A = []
    total = 0
    for u, v, we in w:
        if find(u) != find(v):
            total += we
            A.append(we)
            union(u, v)
    return A, total

t, w = MST_KRUSKAL(parent, edge)

for i in t:
    print(i, end=" ")
print(w)
