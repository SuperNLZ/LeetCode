#coding=utf-8
# @brief: leetCode 200 题
# @author: BeyondShadow
# @date: 2018/02/01
# @tag: recursion, dfs, bfs

# @brief：直接深搜
class Solution2(object):
    def numIslands(self, grid):
        self.height = len(grid)
        if self.height <= 0:
            return 0
        self.width = len(grid[0])
        self.dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.ans = 0
        self.grid = grid
        for x in range(self.height):
            for y in range(self.width):
                if grid[x][y] == "1":
                    grid[x][y] = "2"
                    self.recursion(x, y)
                    self.ans += 1
        return self.ans
    def recursion(self, x, y):
        for v in range(4):
            _x = x + self.dir[v][0]
            _y = y + self.dir[v][1]
            if not self.checkBoundary(_x, _y):
                if self.grid[_x][_y] == "1":
                    self.grid[_x][_y] = "2"
                    self.recursion(_x, _y)

    def checkBoundary(self, x, y):
        if (x < 0) or (x >= self.height) or (y < 0) or (y >= self.width):
            return True
        return False

# @brief: 常规的广搜
class Solution(object):
    def numIslands(self, grid):
        self.height = len(grid)
        if self.height <= 0:
            return 0
        self.width = len(grid[0])
        self.grid = grid
        self.dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ans = 0
        for x in range(self.height):
            for y in range(self.width):
                if self.grid[x][y] == "1":
                    ans += 1
                    self.grid[x][y] = "0"
                    self.bfs(x, y)
        print ans
        return ans

    def bfs(self, x, y):
        que = [[x, y]]
        while que:
            cur = que.pop()
            x, y = cur[0], cur[1]
            for v in range(4):
                _x = x+self.dir[v][0]
                _y = y+self.dir[v][1]
                self.turn(_x, _y, que)

    def turn(self, x, y, que):
        if self.checkBoundary(x, y):
            return
        if self.grid[x][y] == "1":
            que.append([x, y])
            self.grid[x][y] = "0"

    def checkBoundary(self, x, y):
        if (x < 0) or (x >= self.height) or (y < 0) or (y >= self.width):
            return True
        return False


s = Solution()
params = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]]
s.numIslands(params)