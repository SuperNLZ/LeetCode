#coding=utf-8
# @brief: leetCode 44 题
# @author: BeyondShadow
# @date: 2018/02/03
# @tag: dp
# @tips：关于匹配问题, 两个串的进度不一致, 可开设一个二维数组, 下标分别是两端的进度, 然后针对特殊字符做处理

# @brief：寻找状态转移方程
#         1、设定dp[x][y] 代表截止 s[x-1], p[y-1], 是否匹配
#         2、初值：dp[0][0] = 0, dp[0][y] = dp[0][y-1] and p[y-1] == "*"
#         3、(1)当 p[y-1] == "*" 时, dp[x][y] = dp[x-1][y] and p[y-1] == "*" 或者 dp[x][y-1] and p[y-1]=="*"
#            (2)当 p[y-1] == "*" 是, dp[x-1][y-1] and (s[x-1]==p[y-1] or p[y-1] == "?")
class Solution1(object):
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)
        dp = [[]]*(m+1)
        for v in range(m+1):
            dp[v] = [False]*(n+1)

        dp[0][0] = True
        for v in range(1, n+1):
            dp[0][v] = dp[0][v-1] and p[v-1]=="*"

        for x in range(1, m+1):
            for y in range(1, n+1):
                dp[x][y] = (dp[x-1][y-1] and (s[x-1]==p[y-1] or p[y-1] == "?")) or (dp[x][y-1] and p[y-1]=="*") or (dp[x-1][y] and p[y-1]=="*") 

        # print dp[m][n]
        return dp[m][n]

# @brief：方案分析如Solution1, 最后发现其实, 真正用到的只有上一层数据, 可以把 dp 压缩, 
#         初始化完整 dp 的第一维度之后, 后面的循环要注意 把数组重新初始化为 False, 
#         因为是迭代的关系, 只初始化 dp[cur][0] = False 即可
class Solution(object):
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)
        dp = [[]]*2
        for v in range(2):
            dp[v] = [False]*(n+1)

        dp[0][0] = True
        for v in range(1, n+1):
            dp[0][v] = dp[0][v-1] and p[v-1]=="*"

        cur = 0
        for x in range(1, m+1):
            cur = not cur
            dp[cur][0] = False
            for y in range(1, n+1):
                dp[cur][y] = ( (dp[not cur][y-1] and (s[x-1]==p[y-1] or p[y-1] == "?")) 
                            or (dp[cur][y-1] and p[y-1]=="*") or (dp[not cur][y] and p[y-1]=="*") ) 
        return dp[cur][n]

s0 = Solution()
s = "aa"
p = "****"
s0.isMatch(s, p)

