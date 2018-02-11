#coding=utf-8
# @brief: leetCode 39 题
# @author: BeyondShadow
# @date: 2018/01/16
class Solution(object):
    def combinationSum(self, candidates, target):
        s = candidates
        t = target
        self.ret = []
        self.minNum = s[0]
        for v in s:
            if v < self.minNum:
                self.minNum = v
        
        self.recursion(s, t, t, [], 0)
        print self.minNum, self.ret
        return self.ret

    def recursion(self, s, t, ans, result, level):
        if ans == 0:
            self.ret.append(result[:])
            return
        if ans < self.minNum:
            return

        _len = len(s)
        for k in range(level, _len):
            result.append(s[k])
            ans -= s[k]
            self.recursion(s, t, ans, result, k)
            ans += s[k]
            result.pop()
            
s = Solution()
s.combinationSum([2, 3, 6, 7], 7)
