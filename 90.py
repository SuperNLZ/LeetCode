#coding=utf-8
# @brief: leetCode 90 题
# @author: BeyondShadow
# @date: 2018/01/19

# @brief：常规的递归思路，只是去重有点蛋疼
class Solution(object):
    def subsetsWithDup(self, nums):
        self.len = len(nums)
        self.ret = dict()
        level = 0
        result = []
        self.recursion(nums, level, result)
        ret = []
        print self.ret
        for k, v in self.ret.items():
            if self.ret[k] is not None:
                ret.append(list(k))
                self.checkDuplicate(k, self.ret[k])
        print ret
        return ret

    def checkDuplicate(self, index, setnums):
        for k, v in self.ret.items():
            if len(index) == len(k) and setnums == self.ret[k]:
                if len(index) > 0 and reduce(lambda x, y: x+y, list(index)) == reduce(lambda x, y: x+y, list(k)):
                    self.ret[k] = None

    def recursion(self, nums, level, result):
        if level  >= self.len:
            _result = tuple(result[:])
            if self.ret.get(_result) is None:
                self.ret[_result] = set(_result)
            return
        for v in range(level, self.len):
            result.append(nums[v])
            self.recursion(nums, v+1, result)
            result.pop()
            self.recursion(nums, v+1, result)
        
s = Solution()
# params = [4,4,4,1,4]
params = [1,1,2,2]
s.subsetsWithDup(params)