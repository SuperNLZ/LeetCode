#coding=utf-8
# @brief: leetCode 116 题
# @author: BeyondShadow
# @date: 2018/01/29
# @Tag: recursion

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

# @brief: 利用完全二叉树的性质, 子几点编号为n, 左孩子为 2*n, 右孩子为 2*n+1
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        self.ret = dict()
        self.maxIdx = 1
        index = 1
        self.ret[index] = root
        self.recursion(root, index)
        depth = self.getDepth(self.maxIdx)
        self.setNextPointer(depth)
        print depth

    def setNextPointer(self, depth):
        for v in range(0, depth):
            start = pow(2, v)
            end = pow(2, v+1)-1
            while start < end:
                self.ret[start].next = self.ret[start+1]
                start += 1

    def recursion(self, root, index):
        if root.left is None:
            return
        self.ret[2*index] = root.left
        self.ret[2*index+1] = root.right
        if 2*index+1 > self.maxIdx:
            self.maxIdx = 2*index+1
        self.recursion(root.left, 2*index)
        self.recursion(root.right, 2*index+1)

    def getDepth(self, num):
        for v in range(num+1):
            if pow(2, v) >= num+1:
                return v

# @brief: 比递归实现起来要简单很多
#         1、利用left 来控制深度
#         2、下一层依赖上次层的父节点的next, 递推过去即可
class Solution2:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        while root.left:
            curNode = root
            while curNode:
                curNode.left.next = curNode.right
                if curNode.next:
                    curNode.right.next = curNode.next.left
                curNode = curNode.next
            root = root.left

s = Solution()



