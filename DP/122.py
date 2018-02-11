#coding=utf-8
# @brief: leetCode 122 题
# @author: BeyondShadow
# @date: 2018/02/08
# @tag: dp


# @brief: 求一个数组相邻切递增的元素差值之和, 
#         值得一提的是, 卖出和下一次买入可以是同一天
class Solution(object):
    def maxProfit(self, prices):
        _len = len(prices)
        if _len < 2:
            return 0

        ans = 0
        minNum = prices[0]
        for x in range(_len):
            if prices[x] > minNum:
                ans += (prices[x] - minNum)
                minNum = prices[x]
            else:
                minNum = prices[x]
        return ans


s = Solution()
nums = [2, 1, 4]
s.maxProfit(nums)