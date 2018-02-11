#coding=utf-8
# @brief: leetCode 100 题
# @author: BeyondShadow
# @date: 2018/01/23
# @Tag: recursion

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @brief: 前、中、后序 随便哪种直接遍历改树, 遇到不同的, 返回就可以了
#         没有什么意义，就懒得去优化了
class Solution(object):
    def isSameTree(self, p, q):
        flag1 = p is None
        flag2 = q is None
        if flag1 + flag2 == 1:
            return False
        elif flag1 + flag2 == 2:
            return True
        self.flag = False
        self.travelTree(p, q)
        return not self.flag

    def travelTree(self, root1, root2):
        if self.flag:
            return 
        if root1.val != root2.val:
            self.flag = True
            return 
        flag1 = root1.left is None
        flag2 = root2.left is None
        flag3 = root1.right is None
        flag4 = root2.right is None
        if flag1 + flag2 == 1 or flag3 + flag4 == 1:
            self.flag = True
            return

        if root1.left is not None:
            self.travelTree(root1.left, root2.left)
        if root1.right is not None:
            self.travelTree(root1.right, root2.right)

    def createTree(self, nums, root):
        _len = len(nums)
        if _len > 0:
            root.left = TreeNode(nums[0])
            self.createTree(nums[2:], root.left)
        if _len > 1:
            root.right = TreeNode(nums[1])
            self.createTree(nums[4:], root.right)

s = Solution()
p = [1, 2, 3, 4]
q = [1, 2, 3, 4]
s.root1 = TreeNode(p[0])
s.createTree(p[1:], s.root1)
s.root2 = TreeNode(q[0])
s.createTree(q[1:], s.root2)
s.isSameTree(s.root1, s.root2)
