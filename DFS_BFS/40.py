#coding=utf-8
# @brief: leetCode 40 题
# @author: BeyondShadow
# @date: 2018/01/16
class Solution(object):
    def combinationSum2(self, candidates, target):
        s = candidates
        t = target
        s.sort()
        self.ret = []
        self.minNum = s[0]
        for v in s:
            if v < self.minNum:
                self.minNum = v
        
        self.recursion(s, t, t, [], 0)
        self.check = dict()
        ret = []
        for v in self.ret:
            tmp = tuple(v)
            if tmp not in self.check:
                self.check[tmp] = True
                ret.append(v)

        print ret
        return ret

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
            self.recursion(s, t, ans, result, k+1)
            ans += s[k]
            result.pop()
            
s = Solution()
s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
