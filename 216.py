#coding=utf-8
# @brief: leetCode 216 题
# @author: BeyondShadow
# @date: 2018/01/18

class Solution(object):
    def combinationSum3(self, k, n):
        self.ret = []
        level = 1
        result = []
        self.recursion(k, n, level, result)
        # print self.ret
        return self.ret

    def recursion(self, k, ans, level, result):
        # print ans, "*****", result
        _len = len(result)
        if _len == k and ans == 0:
            self.ret.append(result[:])
        if _len > k:
            return 
        if ans < level:
            return 

        for v in range(level, 10):
            result.append(v)
            self.recursion(k, ans-v, v+1, result)
            result.pop()

s = Solution()
s.combinationSum3(3, 9)