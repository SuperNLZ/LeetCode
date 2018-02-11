#coding=utf-8
# @brief: leetCode 101 题
# @author: BeyondShadow
# @date: 2018/01/26
# @Tag: recursion, BST, Balanced

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @brief：关键在于弄清楚如何去比较
#         因为要求是对称, 从根节点开始, 左孩子向左走到底, 右孩子向右走到
class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.recursion(root.left, root.right)
        
    def recursion(self, left, right):
        flag1 = left is None
        flag2 = right is None
        if flag1 + flag2 == 2:
            return True
        elif flag1 + flag2 == 1:
            return False
        elif flag1 + flag2 == 0 and left.val != right.val:
            return False
        return self.recursion(left.left, right.right) and self.recursion(left.right, right.left)

