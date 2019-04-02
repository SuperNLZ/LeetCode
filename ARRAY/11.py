#coding=utf-8
# @brief: leetCode 11 题
# @author: shadow
# @date: 2019/04/02
# @tag: dp

# @brief: 题意：给定一个数组，任意两个数组之间下标的间隔作为width，这两个元素中间的较小值作为高度
#              组成一个矩形，计算面积。计算这个数组满足条件的最大面积值。
#         思路：1、从左右两边开始往中间走，此时间隔最大，计算面积; 2、如果左值较小, 左下标+1, 如果右值较小, 右下标-1
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        _len = len(height)
        i, j, width = 0, _len-1, _len - 1
        while i<j:
            width = min(height[i], height[j])
            ans = max((j-i) * width, ans)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return ans


s = Solution()

height = [1,8,6,2,5,4,8,3,7]
ans = s.maxArea(height)
print("show ans: ", ans)
