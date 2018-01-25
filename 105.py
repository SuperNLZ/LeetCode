#coding=utf-8
# @brief: leetCode 105 题
# @author: BeyondShadow
# @date: 2018/01/24
# @Tag: recursion

# @brief: 1、前序序列的第一个元素为该树的根节点
#         2、根节点在中序中位置的左边是左子树, 右边是右子树
#         3、通过左子树和右子树的节点个数, 在前序中找到对应的前序序列
#         4、有了左子树和右子树的前序和中序序列, then？开始递归吧
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        root = self.recursion(preorder, inorder)
        self.travelTree(root)
        return root

    def recursion(self, preorder, inorder):
        _len = len(preorder)
        if _len == 0:
            return None
        root = preorder[0]
        treeNode = TreeNode(root)
        if _len == 1:
            return treeNode
        pos = inorder.index(root)
        _preorder = preorder[1:pos+1]
        _inorder = inorder[:pos]
        treeNode.left = self.recursion(_preorder, _inorder)
        _preorder = preorder[pos+1:_len]
        _inorder = inorder[pos+1:_len]
        treeNode.right = self.recursion(_preorder, _inorder)
        return treeNode

    def travelTree(self, root):
        if root is None:
            return
        if root.left is not None:
            print "left"
            self.travelTree(root.left)
        if root.right is not None:
            print "right"
            self.travelTree(root.right)

s = Solution()
# p = [1, 3, 5, 2, 4]
# q = [5, 3, 1, 2, 4]
# p = [2, 1, 3]
# q = [1, 2, 3]
p = []
q = []
s.buildTree(p, q)