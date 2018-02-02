#coding=utf-8
# @brief: leetCode 133 题
# @author: BeyondShadow
# @date: 2018/02/01
# @tag: recursion, dfs, bfs

'''
题目大意：给定一个无向图, 图中的节点结构已指定, 要求复制一个完全一样的图;
          题目中给出了一些信息起到了干扰作用, 真正只需要把输入的node 复制下来, 
          然后处理他的 neighbors 就可以了.
          在遍历 neighbors 的过程中, 可能有些节点已经复制过, 使用dict把复制过的节点保存下来
'''

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

# @brief: 深搜算法
class Solution1:
    def cloneGraph(self, node):
        if node is None:
            return
        head = UndirectedGraphNode(node.label)
        self.ret = dict(node = head)
        self.dfs(head, node)
        return head

    def dfs(self, head, node):
        if not node.neighbors:
            return
        for neighbor in node.neighbors:
            if neighbor in self.ret:
                head.neighbors.append(self.ret[neighbor])
            else:
                cur = UndirectedGraphNode(neighbor.label)
                head.neighbors.append(cur)
                self.ret[neighbor] = cur
                self.dfs(cur, neighbor)


# @brief：广搜算法
class Solution:
    def cloneGraph(self, node):
        if node is None:
            return
        head = UndirectedGraphNode(node.label)
        self.ret = dict(node = head)
        self.bfs(head, node)
        return head

    def bfs(self, head, node):
        que = [[head, node]]
        while que:
            cur = que.pop()
            for neighbor in cur[1].neighbors:
                if neighbor in self.ret:
                    cur[0].neighbors.append(self.ret[neighbor])
                else:
                    _cur = UndirectedGraphNode(neighbor.label)
                    cur[0].neighbors.append(_cur)
                    self.ret[neighbor] = _cur
                    que.append([_cur, neighbor])