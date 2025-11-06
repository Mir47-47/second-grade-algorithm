class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def treeInsert(self, t: int):
        self._treeInsert(self.root, t)
    def _treeInsert(self, t: Node, x: int) :
        r=Node(x)
        if(self.root is None):
            self.root = r
            return
        else:
            p = None
            temp = t
            while temp != None:
                p = temp
                if r.key < temp.key:
                    temp = temp.left
                else:
                    temp = temp.right
            if(r.key < p.key):
                p.left = r
            else:
                p.right = r
    def treeDelete(self, key):
        self.root = self._treeDelete(self.root, key)


    def _treeDelete(self, node: Node, key: int) -> Node:
        if node is None:
            return node
        if key < node.key:
            node.left = self._treeDelete(node.left, key)
        elif key > node.key:
            node.right = self._treeDelete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
        return node


    def treePrint(self, node, depth=0):
        if node is None:
            return

        print(depth*4*' '+ str(node.key))

        self.treePrint(node.left, depth + 1)

        self.treePrint(node.right, depth + 1)



n = int(input())
tree = BinarySearchTree()
for i in range(n):
    command = list(input().split())
    if(command[0] == "D"):
        tree.treeDelete(int(command[1]))
    elif(command[0] == "I"):
        tree.treeInsert(int(command[1]))

tree.treePrint(tree.root)




