#coding=utf-8
# @brief: leetCode 17 题
# @author: BeyondShadow
# @date: 2018/01/18
# @tag:递归

class Solution(object):
    def letterCombinations(self, digits):
        self.map = ("abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz")
        if (not digits) or ("0" in digits) or ("1" in digits):
            return []
        self.len = len(digits)
        self.ret = []
        self.recursion(digits, 0, "")
        # print self.ret
        return self.ret
    def recursion(self, digits, level, result):
        if level > self.len:
            return 
        if level == self.len:
            self.ret.append(result[:])
            return

        strs = self.map[int(digits[level])-2]
        for v in strs:
            result = result + v
            self.recursion(digits, level+1, result)
            result = result[:-1]

s = Solution()
s.letterCombinations("23")