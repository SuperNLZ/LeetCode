#-*- coding: utf-8 -*-

#@Brief:
#@Author:Shadow
#@Date:2011-11-28

from queue import LifoQueue
class Solution1:
    def isValid(self, s: str) -> bool:
        length = len(s)
        push_list = ["(", "{", "["]
        que = LifoQueue()
        for x in range(length):
            if s[x] in push_list:
                que.put(s[x])
                continue
            if que.empty():
                return False
            if not self.isMatch(que.get(), s[x]):
                return False
        return que.empty()

    def isMatch(self, left, right):
        match_list = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        return match_list.get(left, None) == right

class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if length % 2 != 0:
            return False
        left_map = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        que = []
        for x in range(length):
            if left_map.get(s[x], None) != None:
                que.append(s[x])
                continue
            if len(que) == 0:
                return False
            if left_map[que[-1]] != s[x]:
                return False
            que.pop()
        return len(que) == 0

msg = "()[]{}"
s = Solution()
print(s.isValid(msg))