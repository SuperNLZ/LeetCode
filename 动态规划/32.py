#coding=utf-8
# @brief: leetCode 32 题
# @author: BeyondShadow
# @date: 2018/02/02
# @tag: dp

# @brief：很逗比的一种做法, 把多余的左括号和右括号都去掉
#         因为字符串不支持该操作, 先转成 list
class Solution1(object):
    def longestValidParentheses(self, s):
        _len = len(s)
        if _len <= 1:
            return 0
        leftNum = 0
        ret = [0]*_len
        for v in range(_len):
            if s[v] == ")":
                ret[v] = 2
            else:
                ret[v] = 1

        for v in range(_len):
            if ret[v] == 2:
                if leftNum <= 0:
                    ret[v] = 3
                    leftNum = 0
                else:
                    leftNum -= 1
            else:
                leftNum += 1

        leftNum = 0
        ret = ret[::-1]
        for v in range(_len):
            if ret[v] == 1:
                if leftNum <= 0:
                    ret[v] = 3
                    leftNum = 0
                else:
                    leftNum -= 1
            else:
                leftNum += 1

        leftNum = 0
        ans = 0
        MIN_INF = -0x7fffffff
        maxSum = MIN_INF
        for v in range(_len):
            if ret[v] == 1:
                if leftNum <= 0:
                    leftNum = 0
                    ans = 0
                else:
                    ans += 1
                    leftNum -= 1
                    if ans > maxSum:
                        maxSum = ans
            elif ret[v] == 2:
                leftNum += 1
            else:
                leftNum = 0
                ans = 0
        if maxSum == MIN_INF:
            maxSum = 0

        return maxSum*2


# @brief: 栈：cur 记录正常匹配的最左端下标, 遇到左括号入栈, 遇到有括号, 判断：
#         1、如果栈空, 更新cur
#         2、如果栈非空, 出栈:(1)栈空, cur 跟当前坐标做对比; (2)栈非空, 当前栈顶元素跟当前元素做对比
class Solution2(object):
    def longestValidParentheses(self, s):
        _len = len(s)
        if _len <= 1:
            return 0
        maxSum = 0
        ret = []
        cur = 0
        for v in range(_len):
            if s[v] == "(":
                ret.append(v)
            else:
                if not ret:
                    cur = v+1
                else:
                    top = ret.pop()
                    if ret:
                        maxSum = max(maxSum, v-ret[-1])
                    else:
                        maxSum = max(maxSum, v-cur+1)
        print maxSum
        return maxSum

# @brief：动态规划, 关键在于如何寻找状态转移方程
#         1、dp[i] 用来保存, 以第 i 个元素结尾的最长长度
#         2、然后判断 s[i-1 -dp[i-1]]==s[i], 
#         3、如果相等 dp[i] = dp[i-1] + 2, 然后再加上 dp[i-dp[i]]
#         4、如果 s[i-1-dp[i-1]] == "(" , dp[i-dp[i]] 是 i-1-dp[i-1] 之前匹配成功的长度
#         5、如果 s[i-1-dp[i-1]] != "(" , dp[i] = 0, dp[i-dp[i]] = dp[i] = 0, 最后 dp[i] 还是0 
class Solution(object):
    def longestValidParentheses(self, s):
        maxSum = 0
        s = ")" + s
        _len = len(s)
        dp = [0]*_len
        for i in range(1, _len):
            if s[i] == ")":
                if s[i-1-dp[i-1]] == "(":
                    dp[i] = dp[i-1] + 2
                dp[i] += dp[i-dp[i]]
            maxSum = max(maxSum, dp[i])

        print maxSum
        return maxSum

s = Solution()
params = "())"
s.longestValidParentheses(params)