#coding=utf-8
# @brief: leetCode 98 题
# @author: BeyondShadow
# @date: 2018/01/26
# @Tag: recursion, BST, Balanced

import math
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @brief: 关键在于要理解一点：对于二分排序树, 中序遍历出来的结果是一个递增的序列
class Solution(object):
    def isValidBST(self, root):
        result = []
        self.inorderTravel(root, result)
        _len = len(result)
        if _len <= 1:
            return True
        return all([result[i] < result[i+1] for i in range(_len-1)])

    def inorderTravel(self, root, result):
        if root is None:
            return result

        if root.left:
            self.inorderTravel(root.left, result)

        result.append(root.val)

        if root.right:
            self.inorderTravel(root.right, result)

        return result
