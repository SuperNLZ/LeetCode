#coding=utf-8
# @brief: leetCode 123 题
# @author: BeyondShadow
# @date: 2018/02/08
# @tag: dp


# @brief: O(n2) 不超时才怪
class Solution1(object):
    def maxProfit(self, prices):
        _len = len(prices)
        if _len <= 0:
            return 0
        if _len <= 1:
            ans = self.getMaxProfit(prices)
            return ans

        maxAns = 0
        for x in range( _len):
            ans1 = self.getMaxProfit(prices[:x])
            ans2 = self.getMaxProfit(prices[x:_len])
            if ans1+ans2 > maxAns:
                maxAns = ans1 + ans2
        return maxAns


    def getMaxProfit(self, prices):
        _len = len(prices)
        if _len < 2:
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


# @brief: 正着遍历一遍, 求出第一次交易的最大值; 倒着遍历一遍, 求出第二次交易的最大值
#         把 1~n 拆为 1~x 和 x~n
#         两次遍历其实可以合到一起, 为了逻辑上清楚一点, 就分开吧, 复杂度并没有增加
class Solution2(object):
    def maxProfit(self, prices):
        _len = len(prices)
        if _len <= 0:
            return 0

        form = [0]*_len
        later = [0]*_len
        self.getFormMaxProfit(prices, form)
        self.getLaterMaxProfit(prices, later)
        ans = 0
        for x in range(_len):
            if form[x] + later[x] > ans:
                ans = form[x] + later[x]

        print ans
        return ans


    def getFormMaxProfit(self, prices, form):
        _len = len(prices)
        if _len < 2:
            return 
        ans = 0
        minNum = prices[0]
        for x in range(1, _len):
            if prices[x] < minNum:
                minNum = prices[x]
            else:
                if prices[x] - minNum > ans:
                    ans = prices[x] - minNum
            form[x] = ans


    def getLaterMaxProfit(self, prices, later):
        _len = len(prices)
        if _len < 2:
            return
        ans = 0
        maxNum = prices[_len-1]
        for x in range(1, _len):
            if prices[_len-1-x] > maxNum:
                maxNum = prices[_len-1-x]
            else:
                if maxNum - prices[_len-1-x] > ans:
                    ans = maxNum - prices[_len-1-x]
            later[_len-1-x] = ans


# @brief: 假定四个数组 buy1[x], buy2[x], out1[x], out2[x]
#         分别代表在第 x 个节点第一次买入、第二次买入、第一次卖出、第二次卖出的最大收益
#         设定初值：buy1[0] = buy2[0] = MIN_INF, out1[0] = out2[0]= 0
#         状态转移方程：buy1[x+1] = max(buy1[x], -prices[x]),        out1[x+1] = max(out1[x], buy1[x]+prices[x])
#                       buy2[x+1] = max(buy2[x], out1[x]-prices[x]), out2[x+1] = max(out2[x], buy2[x]+prices[x])
class Solution3(object):
    def maxProfit(self, prices):
        _len = len(prices)
        if _len < 2:
            return 0
        MIN_INF = -0x7fffffff
        buy1 = [MIN_INF]*(_len+1)
        buy2 = [MIN_INF]*(_len+1)
        out1 = [0]*(_len+1)
        out2 = [0]*(_len+1)
        for x in range(_len):
            buy1[x+1] = max(buy1[x], -prices[x])
            out1[x+1] = max(out1[x], buy1[x]+prices[x])
            buy2[x+1] = max(buy2[x], out1[x]-prices[x])
            out2[x+1] = max(out2[x], buy2[x]+prices[x])

        return out2[_len]


# @brief: 思路类似于 Solution3, 发现四种状态都只与前一状态有关, 
#         这种情况都是可以空间的, 降低数组的维度
class Solution(object):
    def maxProfit(self, prices):
        _len = len(prices)
        if _len < 2:
            return 0
        MIN_INF = -0x7fffffff
        buy1 = MIN_INF
        buy2 = MIN_INF
        out1 = 0
        out2 = 0
        for x in range(_len):
            buy1 = max(buy1, -prices[x])
            out1 = max(out1, buy1+prices[x])
            buy2 = max(buy2, out1-prices[x])
            out2 = max(out2, buy2+prices[x])

        return out2


s = Solution()
prices = [2,1]
s.maxProfit(prices)
