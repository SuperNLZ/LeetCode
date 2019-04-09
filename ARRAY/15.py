#coding=utf-8
# @brief: leetCode 15 题
# @author: shadow
# @date: 2019/04/03
# @tag: dp

# @brief: 题意：给定一个数组，找出其中的三个元素之和为 0 的所有组合，要求组合不能重复
#         思路：1、先排序; 2、外层一个循环, 用于控制第一个元素, 内部两个元素 从两边往中间走
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        _len = len(nums)
        ans = []
        for x in range(_len):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            l, r = x + 1, _len - 1
            while l < r:
                tmp = nums[x] + nums[l] + nums[r]
                if tmp == 0:
                    # print("show x, l, r: ", x, l, r)
                    ans.append([nums[x], nums[l], nums[r]])
                    while (l < _len-1) and (nums[l] == nums[l+1]):
                        l += 1
                    while (r > 0) and (nums[r] == nums[r-1]):
                        r -= 1
                    l += 1
                elif tmp < 0:
                    l += 1
                else:
                    r -= 1
        return ans

s = Solution()

height = [-1,0,1,2,-1,-4]
ans = s.threeSum(height)
print("show ans: ", ans)
