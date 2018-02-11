#coding=utf-8
# @brief: leetCode 109 题
# @author: BeyondShadow
# @date: 2018/01/26
# @Tag: recursion, BST, Balanced

# @brief: 把list 上 node 的值转成排好序的列表，然后同 108
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        nums = self.convertToNums(head)
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

    def convertToNums(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return nums