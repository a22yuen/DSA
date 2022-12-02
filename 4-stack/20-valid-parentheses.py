# -----------------------------------------------------------
# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#   Open brackets must be closed by the same type of brackets.
#   Open brackets must be closed in the correct order.
#   Every close bracket has a corresponding open bracket of the same type.
# Example 1:
#   Input: s = "()"
#   Output: true
# Example 2:
#   Input: s = "()[]{}"
#   Output: true
# Example 3:
#   Input: s = "(]"
#   Output: false
# -----------------------------------------------------------
from typing import List
import collections

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "]": "[",  "}": "{"}
        stack = [] 
        for x in s:
            if x in bracket_map:
                if not len(stack) or bracket_map[x] != stack.pop():
                    return False
            else:
                stack.append(x)
        return True if not len(stack) else False

