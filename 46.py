#coding=utf-8
# @brief: leetCode 46 题
# @author: BeyondShadow
# @date: 2018/01/22

class Solution(object):
    def permute(self, nums):
        self.len = len(nums)
        self.ret = []
        result = [[], set()]
        self.recursion(nums, 0, result)
        print len(self.ret)
        return self.ret

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


s = Solution()
params = [1, 2, 3, 4, 5]
s.permute(params)