#coding=utf-8
# @brief: leetCode 304 题
# @author: BeyondShadow
# @date: 2018/02/12
# @tag: dp


# @brief: 很简单的做法了, dp[x][y] 表示: 第 i 行, 第0列到第 y 列的和
class NumMatrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.m = len(matrix)
        if self.m < 1:
            return 
        self.n = len(matrix[0])
        self.dp = [0]*self.m
        for x in range(self.m):
            self.dp[x] = [0]*self.n

        for x in range(self.m):
            self.dp[x][0] = matrix[x][0]

        for x in range(self.m):
            for y in range(self.n):
                self.dp[x][y] = self.dp[x][y-1] + matrix[x][y]

    def sumRegion(self, row1, col1, row2, col2):
        if self.m < 0:
            return 0
        ans = 0
        for x in range(row1, row2+1):
            ans += self.dp[x][col2] - self.dp[x][col1] + self.matrix[x][col1]

        return ans


nums1 = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
nums = [[-4,-5]]
s = NumMatrix(nums)
s.sumRegion(0, 0, 0, 1)
