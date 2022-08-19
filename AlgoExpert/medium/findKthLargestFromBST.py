# This is an input class. Do not edit.

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    if tree is None:
        return
    values = []
    values.extend(getValueList(tree))

    return values[k]

def getValueList(tree):
    if tree is None:
        return
    values = []
    # left
    values.extend(getValueList(tree.left))
    if not (tree.value in values):
        values.append(tree.value)
    # right
    values.extend(getValueList(tree.right))
    return values
