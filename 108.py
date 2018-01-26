#coding=utf-8
# @brief: leetCode 106 题
# @author: BeyondShadow
# @date: 2018/01/26
# @Tag: recursion, BST, Balanced

# @brief: 1、BST：二叉排序树：左子树的所有节点上的值肯定小于根节点的值, 
#                 右子树的所有节点的值肯定大于根节点的值
#         2、平衡树：左、右子树的高度差不超过 1
#         3、可能树的结构是不同的, 最开始没有理解清楚, 坑了直接

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        root = self.recursion(nums)
        return root

    def recursion(self, nums):
        _len = len(nums)
        if _len <= 0:
            return 
        if _len == 1:
            treeNode = TreeNode(nums[0])
            return treeNode

        pos = _len/2                           #优先左节点
        # pos = int(math.ceil(1.0*_len/2))-1   #优先右节点
        treeNode = TreeNode(nums[pos])
        treeNode.left = self.recursion(nums[:pos])
        treeNode.right = self.recursion(nums[pos+1:])
        return treeNode


s = Solution()
params = [1, 2, 3, 4]
s.sortedArrayToBST(params)