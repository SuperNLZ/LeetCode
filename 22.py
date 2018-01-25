#coding=utf-8
# @brief: leetCode 22 题
# @author: BeyondShadow
# @date: 2018/01/19

# @brief：常规的递归题目, 不过要注意一下退出条件
class Solution(object):
    def generateParenthesis(self, n):
        strs = "()"
        counts = dict()
        counts["("] = 0
        counts[")"] = 0
        self.ret = []
        self.recursion(strs, n, 0, "", counts)
        # print self.ret
        return self.ret

    def recursion(self, strs, n, level, result, counts):
        if level > 2*n:
            return 
        if counts["("] < counts[")"]:
            return 
        if counts["("] > n:
            return 
        if level == 2*n and counts["("] == counts[")"]:
            self.ret.append(result[:])
            return 
        for k in range(0, 2):
            counts[strs[k]] += 1
            result += strs[k]
            self.recursion(strs, n, level+1, result, counts)
            counts[strs[k]] -= 1
            result = result[:-1]


s = Solution()
s.generateParenthesis(3)



