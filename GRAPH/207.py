#coding=utf-8
# @brief: leetCode 207 题
# @author: BeyondShadow
# @date: 2018/01/30
# @Tag: graph, degree

# @brief: 在有向图中判断是否有环存在
#         degree 中保存在节点的出度, que 中保存着所有出度为 0 的节点
#         遍历 que 中的节点, 删除掉并修改相关节点的出度
#         最终判断是否所有的节点出度都为 0
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        ret = []
        degree = dict()
        for v in range(numCourses):
            ret.append(0)
            degree[v] = []
        for v in prerequisites:
            ret[v[0]] += 1
            degree[v[1]].append(v[0])
        que = set()
        for k, v in enumerate(ret):
            if v == 0:
                que.add(k)
        count = len(que)
        while(que):
            k = que.pop()
            nodes = degree[k]
            if nodes:
                for v in nodes:
                    ret[v] -= 1
                    if ret[v] == 0:
                        que.add(v)
                        count += 1
        return count == numCourses

s = Solution()

num = 4
prere = [[1,0],[0,2],[2,3]]
print s.canFinish(num, prere)
