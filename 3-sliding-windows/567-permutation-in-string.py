# -----------------------------------------------------------
# 567. Permutation in String
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.
# Example 1:
#  Input: s1 = "ab", s2 = "eidbaooo"
#  Output: true
#  Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
#  Input: s1 = "ab", s2 = "eidboaoo"
#  Output: false
# -----------------------------------------------------------
from typing import List
import collections

# SLiding window size of s1
# Can be made faster with array

# Get counter of s1 and compare with substring of equal length in s2
# Update s2 substring counter by changing count with left and right index to save time with sliding window


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = collections.Counter(s1)
        left, right = 0, len(s1)-1
        s = s2[left:right+1]
        w = collections.Counter(s)
        while right < len(s2):
            if d == w:
                return True
            w[s2[left]] -= 1
            right += 1
            if right < len(s2):
                w[s2[right]] += 1
            left += 1
        return False
