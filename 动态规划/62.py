#coding=utf-8
# @brief: leetCode 62 题
# @author: BeyondShadow
# @date: 2018/02/02
# @tag: dp

class Solution(object):
    def uniquePaths(self, m, n):
        dp = []
        for x in range(m):
            dp.append([])
            for y in range(n):
                num = 0
                if x == 0 or y == 0:
                    num = 1
                dp[x].append(num)

        for x in range(1, m):
            for y in range(1, n):
                dp[x][y] = dp[x-1][y] + dp[x][y-1]

        return dp[m-1][n-1]

s = Solution()
s.uniquePaths(3, 7)
