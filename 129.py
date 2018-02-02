#coding=utf-8
# @brief: leetCode 129 题
# @author: BeyondShadow
# @date: 2018/01/31
# @tag: recursion

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @brief：很简单的一道递归题目
#         1、判断左孩子是不是叶子节点, 如果是加上根节点到左孩子所组成的数字, 如果不是, 递归左子树
#         2、右孩子等同左孩子
class Solution(object):
    def sumNumbers(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        self.ans = 0
        self.val = root.val
        self.recursion(root, root.val)
        return self.ans

    def recursion(self, root, result):
        if root.left is not None:
            if root.left.left is not None or root.left.right is not None:
                self.recursion(root.left, 10*result+root.left.val)
            else:
                self.ans += 10*result+root.left.val

        if root.right is not None:
            if root.right.left is not None or root.right.right is not None:
                self.recursion(root.right, 10*result+root.right.val)
            else:
                self.ans += 10*result+root.right.val

