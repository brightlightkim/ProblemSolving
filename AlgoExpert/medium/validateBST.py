# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def validateBst(tree):

    if not bstHelper(tree.left, None, tree.value):
        return False
    if not bstHelper(tree.right, tree.value, None):
        return False
    return True

def bstHelper(tree, leftMost=None, rightMost=None):
    if not tree:
        return
    # check basic case
    if (leftMost is not None and tree.value < leftMost) or (rightMost is not None and tree.value > rightMost):
        return False
    # check the basic case
    if (tree.left and tree.left.value >= tree.value) or (tree.right.value and tree.right.value < tree.value):
        return False

    # determine leftMost and rightMost
    if not rightMost:
        rightMost = tree.value
    else:
        if tree.value > rightMost:
            rightMost = tree.value
    if not leftMost:
        leftMost = tree.value
    else:
        if tree.value < leftMost:
            leftMost = tree.value

    # move left
    if not bstHelper(tree.left, leftMost, rightMost):
        return False
    # move right
    if not bstHelper(tree.right, leftMost, rightMost):
        return False
    return True