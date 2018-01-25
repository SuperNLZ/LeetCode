#coding=utf-8
# @brief: leetCode 47 题
# @author: BeyondShadow
# @date: 2018/01/22

# @brief: 用下标表示数据，求出所有的排列后, 再去重
#         python 中最简单的去重方式就是用tuple和dict搭配
class Solution(object):
    def permuteUnique(self, nums):
        self.len = len(nums)
        cnums = range(1, self.len+1)
        self.ret = []
        level = 0
        result = [[], set()]
        self.recursion(cnums, level, result)
        # print self.ret
        ans = []
        self.duplicates = dict()
        for v in self.ret:
            # 普通的append 方式, 每次追加元素都要对list的数据结构做修改
            # 列表解析 的方式, 在一开始初始化好数据结构, 要快一些
            ret = [nums[_v-1] for _v in v]     
            # ret = []
            # for _v in v:
            #     ret.append(nums[_v-1])
            if not self.checkDuplicate(ret):
                ans.append(ret)
        return ans

    def recursion(self, nums, level, result):
        if level > self.len:
            return
        if level == self.len:
            self.ret.append(result[0][:])
            return

        for v in range(0, self.len):
            if nums[v] not in result[1]:
                result[0].append(nums[v])
                result[1].add(nums[v])
                self.recursion(nums, level+1, result)
                result[0].pop()
                result[1].remove(nums[v])

    def checkDuplicate(self, setnums):
        setnums = tuple(setnums)
        if setnums in self.duplicates:
            return True
        self.duplicates[setnums] = True
        return False

s = Solution()
params = [1, 1, 2]
# params = [1,-1,1,2,-1,2,2,-1]
s.permuteUnique(params)