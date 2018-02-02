#coding=utf-8
# @brief: leetCode 199 题
# @author: BeyondShadow
# @date: 2018/02/01
# @tag: recursion

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @brief: 开始还以为要转化成层序遍历, 后来发现想复杂了
#         其实就是求每一层的而最后一个, 先序遍历, 记录当前深度,
#         每一层后面遍历到的节点肯定是在之前遍历到的当前层的节点的右边, 直接覆盖即可
class Solution(object):
    def rightSideView(self, root):
        if root is None:
            return None
        self.ret = dict()
        level = 0
        self.recursion(root, level)
        ret = []
        _len = len(self.ret)
        for v in range(_len):
            ret.append(self.ret[v])
        return ret

    def recursion(self, root, level):
        self.ret[level] = root.val
        if root.left:
            self.recursion(root.left, level+1)
        if root.right:
            self.recursion(root.right, level+1)
