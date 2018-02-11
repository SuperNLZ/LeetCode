#coding=utf-8
# @brief: leetCode 70 题
# @author: BeyondShadow
# @date: 2018/02/03
# @tag: dp

# @brief: 斐波那些数列
class Solution1(object):
    def climbStairs(self, n):
        if n <= 1:
            return 1
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2
        for v in range(2, n):
            dp[v] = dp[v-1] + dp[v-2]

        return dp[n-1]

# @brief: 用不到数组, 直接变量向后叠加就可以了
class Solution(object):
    def climbStairs(self, n):
        if n <= 1:
            return 1
        a = 1
        b = 1
        for v in range(1, n):
            b = a+b
            a = b-a
        return b