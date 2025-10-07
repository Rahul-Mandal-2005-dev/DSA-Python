class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def postOrder(arr, idx):
    idx[0] += 1
    if (arr[idx[0]] == -1):
        return None
    root = Node(arr[idx[0]])
    root.left = postOrder(arr, idx)
    root.right = postOrder(arr, idx)
    return root


def postOrderTraverse(root):
    temp = root
    if (root == None):
        return
    postOrderTraverse(temp.left)
    postOrderTraverse(temp.right)
    print(temp.data, end="--->")


arr = [1, 2, 3, -1, -1, 4, -1, -1, 5, -1, -1]
idx = [-1]
root = postOrder(arr, idx)
postOrderTraverse(root)
print("None")
