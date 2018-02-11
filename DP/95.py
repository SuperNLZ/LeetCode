#coding=utf-8
# @brief: leetCode 95 题
# @author: BeyondShadow
# @date: 2018/02/03
# @tag: dp

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        if n < 1:
            return []
        ret = self.recursion(1, n)
        return ret
    def recursion(self, left, right):
        if left > right:
            return [None]
        if left == right:
            cur = TreeNode(left)
            return[cur]
        ret = []
        for x in range(left, right+1):
            leftRet = self.recursion(left, x-1)
            rightRet = self.recursion(x+1, right)
            for y in leftRet:
                for z in rightRet:
                    cur = TreeNode(x)
                    cur.left = y
                    cur.right = z
                    ret.append(cur)
        return ret

s = Solution()
s.generateTrees(3)
