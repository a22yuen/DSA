# -----------------------------------------------------------
# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:
#   Input: s = "anagram", t = "nagaram"
#   Output: true
# Example 2:
#   Input: s = "rat", t = "car"
#   Output: false
# -----------------------------------------------------------

# 2 hash tables
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for x in s:
            if x not in d:
                d[x] = 1
            else:
                d[x] = d[x] + 1
        for x in t:
            if x not in d:
                return False
            else:
                d[x] = d[x]-1

        for k, v in d.items():
            if v is not 0:
                return False
        return True
