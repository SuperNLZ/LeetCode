#coding=utf-8
# @brief: leetCode 96 题
# @author: BeyondShadow
# @date: 2018/02/02
# @tag: dp

# @brief: 关键在于状态转移方程
#         我们假设 n 个节点, 其中一个为根节点, 则ans = ans(左子树) * ans(右子树)
#         也就是说, n 个节点, 去掉一个, 剩下 n-1 个, 左右孩子分配即可
#         dp[n] = dp[0]*dp[n-1] + dp[1]*dp[n-2] + ... + dp[n-2]d[1] + dp[n-1][0]
class Solution(object):
    def numTrees(self, n):
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        for x in range(2, n+1):
            for y in range(x):
                dp[x] +=  dp[y]*dp[x-y-1]

        return dp[n]

s = Solution()
s.numTrees(5)