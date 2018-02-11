#coding=utf-8
# @brief: leetCode 303 题
# @author: BeyondShadow
# @date: 2018/02/03
# @tag: dp

# @brief: 动态转移方程：dp[x] = dp[x-1] + nums[x]
#         最开始想复杂了, 用了二维数组, dp[x][y] = dp[0][y] - dp[0][x-1]
#         其实用不到这么复杂, 而且这样做初始化dp数组的复杂度是 O(n2), 
#         采用一维数组, 在调用 sumRange 的时候, 计算一下 dp[j] - dp[i-1]
#         复杂度直接降到 O(n)
class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
        self.m = len(nums)
        if self.m < 1:
            return 
        dp = [0]*self.m
        dp[0] = nums[0]
        for x in range(1, self.m):
            dp[x] = dp[x-1] + nums[x]
        self.dp = dp
        # print dp

    def sumRange(self, i, j):
        if self.m < 1:
            return [None]
        if i < 1:
            return self.dp[j]
        return self.dp[j] - self.dp[i-1]