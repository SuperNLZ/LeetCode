#coding=utf-8
# @brief: leetCode 124 题
# @author: BeyondShadow
# @date: 2018/01/31
# @Tag: recursion

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @brief: 先先序遍历, 保存遍历到的值, 
#         然后遍历数组, 创建节点, 就是有点浪费空间
class Solution(object):
    def flatten(self, root):
        if root is None:
            return None
        result = []
        self.preOrderTravel(root, result)
        self.resetRoot(root, result)
        print result

    def preOrderTravel(self, root, result):
        if root is None:
            return 
        result.append(root.val)
        self.preOrderTravel(root.left, result)
        self.preOrderTravel(root.right, result)

    def resetRoot(self, root, result):
        _len = len(result)
        for v in range(1, _len):
            root.left = None
            root.right = TreeNode(result[v])
            root = root.right

# @brief：相比第一种方法, 节省了空间, 但在一定程度上浪费了时间
#         关键在于找规律：根节点如果有左子树, 则左子树的先序遍历的最后一个节点 应该是跟几点右孩子的父节点
#                         根节点 的右节点为左孩子. 
#         最后要变成一个链表的形式, 遍历的时候只要给每个赋予右孩子即可
class Solution2(object):
    def flatten(self, root):
        self.recursion(root)

    def recursion(self, root):
        if root is None:
            return
        if root.left is not None:
            curNode = root.left
            while curNode.right:
                curNode = curNode.right
            curNode.right = root.right
            root.right = root.left
            root.left = None
        self.recursion(root.right)