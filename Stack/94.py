#-*- coding: utf-8 -*-

#@Brief:
#@Author:Shadow
#@Date:2011-11-28

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal1(self, root: TreeNode) -> [int]:
        if not root:
            return[]
        if not root.left:
            if not root.right:
                return [root.val]
            else:
                return [root.val] + self.inorderTraversal(root.right)
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal(self, root: TreeNode) -> [int]:
        ans = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            top = stack.pop()
            ans.append(top.val)
            root = top.right
        return ans
msg = "()[]{}"
s = Solution()
print(s.isValid(msg))