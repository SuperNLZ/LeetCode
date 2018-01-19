#coding=utf-8
# @brief: leetCode 78 题
# @author: BeyondShadow
# @date: 2018/01/19

# @brief: 比较简单的一道题目, 老套路, 遍历数据, 每个元素有选和不选两种情况
#         但是要注意去重
class Solution(object):
    def subsets(self, nums):
        self.len = len(nums)
        self.ret = dict()
        level = 0
        result = []
        self.recursion(nums, level, result)
        ret = []
        for v in self.ret.items():
            ret.append(list(v[0]))
        print ret


    def recursion(self, nums, level, result):
        if level  >= self.len:
            _result = tuple(result[:])
            if self.ret.get(_result) is None:
                self.ret[_result] = True
            return
        for v in range(level, self.len):
            result.append(nums[v])
            self.recursion(nums, v+1, result)
            result.pop()
            self.recursion(nums, v+1, result)

s = Solution()
s.subsets([1,2,2, 2])