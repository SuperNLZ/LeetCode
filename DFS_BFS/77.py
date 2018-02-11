#coding=utf-8
# @brief: leetCode 77 题
# @author: BeyondShadow
# @date: 2018/01/19

class Solution(object):
    def combine(self, n, k):
        self.ret = []
        result = []
        self.recursion(n, k, 1, result)
        # print self.ret
        return self.ret

    def recursion(self, n, k, level, result):
        if len(result) >= k:
            self.ret.append(result[:])
            return
        if n-level+1+len(result) < k:
            return

        for v in range(level, n+1):
            result.append(v)
            self.recursion(n, k, v+1, result)
            result.pop()


s = Solution()
print s.combine(4, 2)
