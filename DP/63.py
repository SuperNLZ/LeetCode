#coding=utf-8
# @brief: leetCode 63 题
# @author: BeyondShadow
# @date: 2018/02/02
# @tag: dp

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        if m <= 0 or obstacleGrid[0][0] == 1:
            return 0
        n = len(obstacleGrid[0])
        dp = obstacleGrid
        dp[0][0] = 1
        for x in range(1, m):
            if dp[x][0] == 0 and dp[x-1][0] == 1:
                dp[x][0] = 1
            else:
                dp[x][0] = 0
        for y in range(1, n):
            if dp[0][y] == 0 and dp[0][y-1] == 1:
                dp[0][y] = 1
            else:
                dp[0][y] = 0

        for x in range(1, m):
            for y in range(1, n):
                if dp[x][y] == 1:
                    dp[x][y] = 0
                else:
                    dp[x][y] = dp[x-1][y] + dp[x][y-1]

        # print dp
        return dp[m-1][n-1]
    

s = Solution()
nums = [[0,0],[1,1],[0,0]]
s.uniquePathsWithObstacles(nums)