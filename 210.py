#coding=utf-8
# @brief: leetCode 210 题
# @author: BeyondShadow
# @date: 2018/01/30
# @Tag: graph, degree

# @brief：跟207题基本一样, 判断路径存在的过程
#         其实就是一条路径是否能行的通,只需把路径记录下来即可
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        ans = []
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
            ans.append(k)
            nodes = degree[k]
            if nodes:
                for v in nodes:
                    ret[v] -= 1
                    if ret[v] == 0:
                        que.add(v)
                        count += 1
        if count != numCourses:
            return 0
        return ans

s = Solution()

num = 3
prere = [[1,0],[1,2],[0,1]]
print s.findOrder(num, prere)
