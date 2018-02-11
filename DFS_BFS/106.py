#coding=utf-8
# @brief: leetCode 106 题
# @author: BeyondShadow
# @date: 2018/01/26
# @Tag: recursion

# @brief: 1、后序序列的最后一个元素为该树的根节点
#         2、根节点在中序中位置的左边是左子树, 右边是右子树
#         3、通过左子树和右子树的节点个数, 在后序中找到对应的后序序列
#         4、有了左子树和右子树的后序和中序序列, then？开始递归吧
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        root = self.recursion(inorder, postorder)
        self.travelTree(root)
        return root

    def recursion(self, inorder, postorder):
        _len = len(inorder)
        if _len == 0:
            return None
        root = postorder[_len-1]
        treeNode = TreeNode(root)
        if _len == 1:
            return treeNode
        pos = inorder.index(root)
        _postorder = postorder[0:pos]
        _inorder = inorder[:pos]
        treeNode.left = self.recursion(_inorder, _postorder)
        _postorder = postorder[pos:_len-1]
        _inorder = inorder[pos+1:_len]
        treeNode.right = self.recursion(_inorder, _postorder)
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
