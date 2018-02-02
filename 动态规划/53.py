#coding=utf-8
# @brief: leetCode 53 题
# @author: BeyondShadow
# @date: 2018/02/02
# @tag: dp

# @brief: 主要是要能拆分子问题
#         其实就是求一段连续的和, 一旦当这段和小于 0 的时候, 这段数字已经不能再往后继续累加了
#         记录这段数字之中的最大值, 然后, 从下一位重新开始累加
class Solution(object):
    def maxSubArray(self, nums):
        ans = 0
        maxSum = -0x7fffffff
        for num in nums:
            if ans < 0:
                ans = 0
            ans += num
            if maxSum < ans:
                maxSum = ans
        # print maxSum
        return maxSum

s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
s.maxSubArray(nums)
