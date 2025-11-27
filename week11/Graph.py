class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

n, m = list(map(int, input().split()))
graph = [[0 for _ in range(m)] for _ in range(n)]
link_graph = [None for _ in range(n)]
array_graph = [[i, []] for i in range(n)]
graph_edge = []

for i in range(0, n):
    for j in range(0, m):
        print(graph[i][j], end=' ')
    print()

k = int(input())
for _ in range(k):
    x, y = list(map(int, input().split()))
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

    if link_graph[x-1] == None:
        link_graph[x-1] = Node(y)
    else:
        curr = link_graph[x-1]
        while curr.next != None:
            curr = curr.next
        curr.next = Node(y)
    if link_graph[y-1] == None:
        link_graph[y-1] = Node(x)
    else:
        curr = link_graph[y-1]
        while curr.next != None:
            curr = curr.next
        curr.next = Node(x)

    array_graph[x-1][0] += 1
    array_graph[x-1][1].append(y)
    array_graph[y-1][0] += 1
    array_graph[y-1][1].append(x)

def DFS(start, visited):
    visited[start] = True
    print(start+1, end=' ')
    for i in range(0, n):
        if graph[start][i] == 1 and not visited[i]:
            DFS(i, visited)

for i in range(0, n):
    for j in range(0, m):
        print(graph[i][j], end=' ')
    print()

# for i in range(0, n):
#     curr = link_graph[i]
#     print(f'Node {i+1}: ', end='')
#     while curr != None:
#         print(f'->{curr.value} ', end='')
#         curr = curr.next
#     print()
#
# for i in range(0, n):
#     print(f'Node {array_graph[i][0]}: ', end='')
#     for j in array_graph[i][1]:
#         print(f'->{j} ', end='')
#     print()

visited = [False for _ in range(n)]
DFS(0, visited)