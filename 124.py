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

# @brief: 假定每个节点都是整数，最大路径，应该是左孩子的最大路径+右孩子的最大路径+根节点的值
#         如果左右孩子的最大路径有负数，就不加.
#         递归的时候：外层递归需要用到内层递归的值，由于路径可以是任意一段路径，用一个全局变量
#                     来做记录，这样，每一颗左、右子树都能跟最大路径值做比较
class Solution(object):
    def maxPathSum(self, root):
        if root is None:
            return 0
        self.ans = -0xfffffff
        self.recursion(root)
    
        return self.ans

    def recursion(self, root):
        if root is None:
            return 0
        curMax = root.val
        leftMax = self.recursion(root.left)
        rightMax = self.recursion(root.right)

        if leftMax > 0:
            curMax += leftMax
        if rightMax > 0:
            curMax += rightMax
        if curMax > self.ans:
            self.ans = curMax
        rootMax = max(max(root.val, root.val+leftMax), root.val+rightMax)
        print root.val, leftMax, rightMax, rootMax
        return rootMax