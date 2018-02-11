#coding=utf-8
# @brief: leetCode 64 题
# @author: BeyondShadow
# @date: 2018/02/03
# @tag: dp

# @brief: 简单的递归, 对python 语言了解不清楚遇到了一个list 的坑
#         对于 python 的 list, 使用乘法的时候, 复制出来的是对象的引用, 而不是新的对象
#         这样使用乘法来创建一维数组是没有问题的, 但是创建二维数组有就问题了
#         L = [[0]*3]*3, L[0][0] = 1, 然后发现 L = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        if m <= 0:
            return 0
        n = len(grid[0])
        dp = [[]]*m
        for x in range(0, m):
            dp[x] = [0]*n

        dp[0][0] = grid[0][0]
        for x in range(1, m):
            dp[x][0] = grid[x][0] + dp[x-1][0]

        for y in range(1, n):
            dp[0][y] = grid[0][y] + dp[0][y-1]

        for x in range(1, m):
            for y in range(1, n):
                dp[x][y] = min(dp[x-1][y], dp[x][y-1]) + grid[x][y]

        return dp[m-1][n-1]

s = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
s.minPathSum(grid)