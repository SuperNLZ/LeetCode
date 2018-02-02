#coding=utf-8
# @brief: leetCode 130 题
# @author: BeyondShadow
# @date: 2018/01/31
# @tag: recursion

# @brief: dfs 爆栈了啊啊啊啊啊啊啊
class Solution2(object):
    def solve(self, board):
        if len(board) <= 0:
            return 
        self.board = board
        self.flag = False
        self.dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.width = len(board[0])
        self.heigth = len(board)
        self.vis = []
        for x in range(self.heigth):
            tmp = []
            for y in range(self.width):
                alphabet = board[x][y]
                if alphabet == "X":
                    tmp.append(1)
                else:
                    tmp.append(0)
            self.vis.append(tmp)
        print self.vis
        for x in range(self.heigth):
            for y in range(self.width):
                if self.vis[x][y] == 0:
                    if self.checkBoundary(x, y):
                        self.flag = True
                    self.vis[x][y] = 1
                    result = [[x,y]]
                    self.recursion(board, x, y, result)
                    if not self.flag:
                        self.turnAlphabet(result)
                self.flag = False
        print self.board

    def recursion(self, board, x, y, result):
        for v in range(4):
            _x, _y = x+self.dir[v][0], y+self.dir[v][1]
            if (_x>=0) and (_x<self.heigth) and (_y>=0) and (_y<self.width) and self.vis[_x][_y] == 0:
                if self.checkBoundary(_x, _y):
                    self.flag = True
                self.vis[_x][_y] = 1
                result.append([_x, _y])

                self.recursion(board, _x, _y, result)

    def checkBoundary(self, x, y):
        if (x==0) or (x==self.heigth-1) or (y==0) or (y==self.width-1):
            return True
        return False

    def turnAlphabet(self, result):
        for v in result:
            self.board[v[0]][v[1]] = "X"

# @brief: 常规的广搜方法, 标记数组, 队列, 但是针对这道题有点复杂了
class Solution1(object):
    def solve(self, board):
        self.board = board
        self.heigth = len(board)
        if self.heigth <= 0:
            return
        self.width = len(board[0])
        self.dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.flag = False
        self.vis = []
        for x in range(self.heigth):
            tmp = []
            for y in range(self.width):
                alphabet = board[x][y]
                if alphabet == "X":
                    tmp.append(1)
                else:
                    tmp.append(0)
            self.vis.append(tmp)
        que = []
        result = []
        for x in range(0, self.heigth):
            for y in range(0, self.width):
                if len(que) == 0:
                    self.turnAlphabet(result)
                    result = []
                    self.flag = False
                if self.vis[x][y] == 0:
                    self.vis[x][y] = 1
                    que.append([x, y])
                    result.append([x, y])
                    if self.checkBoundary(x, y):
                        self.flag = True
                    self.bfs(que, result)

        print self.board

    def bfs(self, que, result):
        while que:
            node = que.pop()
            # print node, "****"
            for v in range(4):
                x = node[0] + self.dir[v][0]
                y = node[1] + self.dir[v][1]
                if not self.beyondBoundary(x, y) and self.vis[x][y] == 0:
                    self.vis[x][y] = 1
                    que.append([x, y])
                    result.append([x, y])
                    if self.checkBoundary(x, y):
                        print "checkBoundary", x, y
                        self.flag = True

    def beyondBoundary(self, x, y):
        if (x < 0) or (x > self.heigth-1) or (y < 0) or (y > self.width-1):
            return True
        return False

    def checkBoundary(self, x, y):
        if (x==0) or (x==self.heigth-1) or (y==0) or (y==self.width-1):
            return True
        return False

    def turnAlphabet(self, result):
        if len(result) == 0:
            return
        if self.flag:
            return 
        for v in result:
            self.board[v[0]][v[1]] = "X"

# @brief：虽然也是广搜, 但是针对本题, 可以反过来思考
#        1、从边上开始搜索，凡是能收到的 "O", 全部转成 "D"
#        2、把所有的 "O" 转成 "X", 再把 "D" 转成 "O"
class Solution:
    def solve(self, board):
        self.board = board
        self.turnRet = []
        self.heigth= len(board)
        if self.heigth <= 0:
            return
        self.width = len(board[0])
        for v in range(self.width):
            self.bfs(0, v)
            self.bfs(self.heigth-1, v)
        for v in range(1, self.heigth-1):
            self.bfs(v, 0)
            self.bfs(v, self.width-1)

        self.turn()
        print self.board

    def bfs(self, x, y):
        que = []
        self.fill(x, y, que)
        while que:
            cur = que.pop()
            x = cur[0]
            y = cur[1]
            self.fill(x-1, y, que)
            self.fill(x+1, y, que)
            self.fill(x, y-1, que)
            self.fill(x, y+1, que)

    def fill(self, x, y, que):
        if (x < 0) or (x >= self.heigth) or (y < 0) or (y >= self.width) or self.board[x][y] != "O":
            return 
        que.append([x, y])
        self.board[x][y] = "D"
        self.turnRet.append([x, y])

    def turn(self):
        for x in range(0, self.heigth):
            for y in range(0, self.width):
                if self.board[x][y] == "O":
                    self.board[x][y] = "X"
        for v in self.turnRet:
            self.board[v[0]][v[1]] = "O"


s = Solution()
params = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# params = []
params = [["O","O","O"],["O","O","O"],["O","O","O"]]
s.solve(params)

