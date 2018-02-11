#coding=utf-8
# @brief: leetCode 60 题
# @author: BeyondShadow
# @date: 2018/01/23
# @Tag: recursion

import math

# @brief：n 的排列数个数是 n!, n 的排列数是 n*(n-1)!
#         可以先确定最高位, 然后问题就转化成了 n-1 个数, 第 _k 个元素
#         这样问题可拆分成子问题, 找到 _k 的表达式, 知道 _k == 1 为止
#         满足递归的两大条件
class Solution(object):
    def getPermutation(self, n, k):
        self.ret = ""
        result = range(1, n+1)
        self.recursion(n, k, result)
        print self.ret
        return self.ret

    def recursion(self, n, k, result):
        if k == 1:
            for v in result:
                self.ret = self.ret + str(v)
            return
        subLen = self.getSubLen(n-1)
        head = int(math.ceil(1.0*k/subLen))
        k = k-(subLen*(head-1))
        head = result[head-1]
        result.remove(head)
        self.ret = self.ret+str(head)
        self.recursion(n-1, k, result)

    def getSubLen(self, n):
        ans = 1
        while(n>1):
            ans *= n
            n -= 1
        return ans

s = Solution()
s.getPermutation(3, 2)