#coding=utf-8
# @brief: leetCode 117 题
# @author: BeyondShadow
# @date: 2018/01/30
# @Tag: recursion, 

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

# @brief: 类似 116, 关键在于找到下一个节点
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        levelNode = None
        nextNode = self.getNextNode(root)
        while nextNode:
            curNode = root
            while curNode:
                if curNode.left:
                    if curNode.right:
                        curNode.left.next = curNode.right
                    elif curNode.next:
                        _nextNode = self.getNextNode(curNode.next)
                        curNode.left.next = _nextNode
                if curNode.right and curNode.next:
                    _nextNode = self.getNextNode(curNode.next)
                    curNode.right.next = _nextNode
                curNode = curNode.next
            root = nextNode
            nextNode = self.getNextNode(root)

    def getNextNode(root):
        if root.left:
            return root.left
        if root.right:
            return root.right
        if root.next is None:
            return 
        return self.getNextNode(root.next)

