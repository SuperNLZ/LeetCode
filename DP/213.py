#coding=utf-8
# @brief: leetCode 213 题
# @author: BeyondShadow
# @date: 2018/02/11
# @tag: dp

'''
题目大意：给出一个由非负数字组成的数组, 求出最大和, 但是不能选中相邻的数字
          不过比 198 相比, 本题的数组是一个环形, 首部和尾部认为是相邻的
'''

# @brief: 直接递推, 因为是环形, 首部和尾部不能同时选取
#         1、不要首部递推一次; 2、不要尾部递推一次; 3、选取较大的
class Solution(object):
    def rob(self, nums):
        _len = len(nums)
        if _len < 1:
            return 0
        if _len == 1:
            return nums[0]
        rob1 = self.getRob(nums[1:])
        rob2 = self.getRob(nums[:_len-1])
        print max(rob1, rob2)
        return max(rob1, rob2)

    def getRob(self, nums):
        _len = len(nums)
        if _len < 1:
            return 0
        if _len == 1:
            return nums[0]
        dp = [0]*_len
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for x in range(2, _len):
            dp[x] = max(dp[x-1], dp[x-2] + nums[x])
        return dp[_len-1]


s = Solution()
nums = [1, 2, 3, 4]
s.rob(nums)