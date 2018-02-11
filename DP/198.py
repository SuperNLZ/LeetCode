#coding=utf-8
# @brief: leetCode 198 题
# @author: BeyondShadow
# @date: 2018/02/11
# @tag: dp

'''
题目大意：给出一个由非负数字组成的数组, 求出最大和, 但是不能选中相邻的数字
'''

# @brief: 直接递推就可以了
class Solution(object):
    def rob(self, nums):
        _len = len(nums)
        if _len < 1:
            return 0
        dp = [0]*_len
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for x in range(2, _len):
            dp[x] = max(dp[x-1], dp[x-2] + nums[x])
        print dp[_len-1]
        return dp[_len-1]


s = Solution()
nums = [1, 2, 3]
s.rob(nums)
