#coding=utf-8
# @brief: leetCode 486 题
# @author: BeyondShadow
# @date: 2018/02/12
# @tag: dp

'''
    题目大意：给出一个数组, 两个选手一次进行选择, 
              1号先选择, 每次都只能在第一位和最后一位中选
              每位选手都尽量使自己最终选取的数字和最大
              返回1号选择的结果能否大于2号
'''


# @brief: 定义数组 dp[x][y] 表示, 第x开始到第y结束的数组中, 1号能剩余的数字和
#         则 1号选择记为 "+", 2号选择记为 "-", 那如果最终 dp[0][n] > 0
#         则 1号选择的结果大于 2号
class Solution(object):
    def PredictTheWinner(self, nums):
        _len = len(nums)
        if _len <= 0:
            return 0
        dp = [0]*_len
        for x in range(_len):
            dp[x] = [0]*_len
        for x in range(_len):
            dp[x][x] = nums[x]

        for x in range(0, _len-1):
            x = _len-2 - x
            for y in range(x+1, _len):
                dp[x][y] = max(nums[x] - dp[x+1][y], nums[y] - dp[x][y-1])

        return dp[0][_len-1] >= 0


s = Solution()
nums = [10,17,11,16,17,9,14,17,18,13,11,4,17,18,15,3,13,9]
nums1 = [1, 5, 2]
s.PredictTheWinner(nums)