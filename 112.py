#coding=utf-8
# @brief: leetCode 112 题
# @author: BeyondShadow
# @date: 2018/01/29
# @Tag: recursion

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @brief：直接递归搜索, 就可以了, 不过要注意, sum 可能是负数
#         之前为了优化, 把 sum 小于0 返回了, 反而错了
class Solution(object):
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        return self.recursion(root, sum-root.val)

    def recursion(self, root, sum):
        if sum == 0 and self.isLeaf(root):
            return True
        # if sum < 0:
        #     return False
        if root is None:
            return False
        if root.left is not None and self.recursion(root.left, sum-root.left.val):
            return True
        if root.right is not None and self.recursion(root.right, sum-root.right.val):
            return True
        return False

    def isLeaf(self, root):
        if root is None:
            return False
        if root.left is not None or root.right is not None:
            return False
        return True

