#coding=utf-8
# @brief: leetCode 121 题
# @author: BeyondShadow
# @date: 2018/02/06
# @tag: dp

# @brief：傻逼一样的做法, 能会不超时吗？以后再写这种代码就去死吧
class Solution1(object):
    def maxProfit(self, prices):
        _len = len(prices)
        maxNum = 0
        for x in range(_len):
            for y in range(x+1, _len):
                if prices[y] - prices[x] > maxNum:
                    maxNum = prices[y] - prices[x]

        return maxNum

# @brief：遍历数组, 更新遍历过程中记录的最小值, 作为买入价
#         如果当前遍历的数值不小于最小值, 可以作为卖出价
#         如果收益高于当前最大收益, 就更新
class Solution(object):
    def maxProfit(self, prices):
        _len = len(prices)
        if _len <= 0:
            return 0
        ans = 0
        minNum = prices[0]
        for x in range(1, _len):
            if prices[x] < minNum:
                minNum = prices[x]
            else:
                if prices[x] - minNum > ans:
                    ans = prices[x] - minNum

        return ans

s = Solution()
prices = [7, 1, 5, 3, 6, 4]
s.maxProfit(prices)