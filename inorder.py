class Node:
    def __init__(self, val: int) -> int:
        self.data = val
        self.left = None
        self.right = None


def inOrder(arr: list[int], idx: list[int]) -> Node:
    idx[0] += 1
    if (arr[idx[0]] == -1):
        return None
    root = Node(arr[idx[0]])
    root.left = inOrder(arr, idx)
    root.right = inOrder(arr, idx)
    return root


def inOrderTraverse(root):
    temp = root
    if (root == None):
        return
    inOrderTraverse(temp.left)
    print(temp.data, end="--->")
    inOrderTraverse(temp.right)


arr: list[int] = [1, 2, 3, -1, -1, 4, -1, -1, 5, -1, -1]
idx: list[int] = [-1]
root: Node = inOrder(arr, idx)

inOrderTraverse(root)
print("None")
