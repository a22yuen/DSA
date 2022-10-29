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

import collections
# 1 hash table
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

        for v in d.values():
            if v is not 0:
                return False
        return True

# Better 2 Hash tables :DDDD
def anagram(s,t):
    sc = collections.Counter(s)
    tc = collections.Counter(t)
    return sc == tc

# This can be done with one hash table by subtracting each
