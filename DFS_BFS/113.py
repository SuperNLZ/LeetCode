#coding=utf-8
# @brief: leetCode 113 题
# @author: BeyondShadow
# @date: 2018/01/29
# @Tag: recursion

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @brief：直接递归搜索, 就可以了, 根112 很类似, 把路径记录下来
class Solution(object):
    def pathSum(self, root, sum):
        if root is None:
            return []
        self.ret = []
        result = []
        result.append(root.val)
        self.recursion(root, sum-root.val, result)
        print self.ret
        return self.ret

    def recursion(self, root, sum, result):
        if sum == 0 and self.isLeaf(root):
            self.ret.append(result[:])
            return
        if root is None:
            return
        if root.left is not None:
            result.append(root.left.val)
            self.recursion(root.left, sum-root.left.val, result)
            result.pop()
        if root.right is not None:
            result.append(root.right.val)
            self.recursion(root.right, sum-root.right.val)
            result.pop()

    def isLeaf(self, root):
        if root is None:
            return False
        if root.left is not None or root.right is not None:
            return False
        return True
