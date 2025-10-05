class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def preOrder(idx, arr):
    idx[0] += 1
    if (arr[idx[0]] == -1):
        return None
    root = Node(arr[idx[0]])
    root.left = preOrder(idx,arr)
    root.right = preOrder(idx,arr)
    return root

def preOrderTraverse(root):
    temp = root
    if(root ==  None):
        return 
    print(temp.data,end="--->")
    preOrderTraverse(temp.left)
    preOrderTraverse(temp.right)

arr = [3, 4, -1, 5, 7, -1, -1, 9, -1, -1, 9, 2, -1, -1, 10, -1, -1]
idx = [-1]
root = preOrder(idx,arr)
preOrderTraverse(root)
print("None")