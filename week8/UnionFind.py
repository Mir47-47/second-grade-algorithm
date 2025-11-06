class Node:
    def __init__(self, k):
        self.key = k
        self.parent = None
        self.rank = 0

def Make_Set(x):
    t = Node(x)
    t.parent = t
    return t

def Union(ix, iy):
    x = Find_set(ix)
    y = Find_set(iy)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank = y.rank + 1

def Find_set(x):
    if x != x.parent:
        x.parent = Find_set(x.parent)
    return x.parent

input_text = list(map(int, input().split()))
n = input_text[0]
m = input_text[1]

nodes = []

for i in range(0, n):
    nodes.append(Make_Set(i))

for i in range(0, m):
    command = list(map(int, input().split()))
    num1 = command[0] - 1
    num2 = command[1] - 1
    Union(nodes[num1], nodes[num2])

maxvalue = [0] * n
for i in range(0, n):
    maxvalue[Find_set(nodes[i]).key] += 1

print(max(maxvalue))

