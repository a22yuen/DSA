# -----------------------------------------------------------
# 567. Permutation in String
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:
# 	Input: s = "cbaebabacd", p = "abc"
# 	Output: [0,6]
# 	Explanation:
# 	The substring with start index = 0 is "cba", which is an anagram of "abc".
# 	The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
#	Input: s = "abab", p = "ab"
#	Output: [0,1,2]
#	Explanation:
#	The substring with start index = 0 is "ab", which is an anagram of "ab".
#	The substring with start index = 1 is "ba", which is an anagram of "ab".
#	The substring with start index = 2 is "ab", which is an anagram of "ab".
# -----------------------------------------------------------
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Sliding window of length p across s. Use array indexed by ascii lowercase characters for O(1) space and time complexity
        # Compare array counter with each other, and each shift down s add and remove the left and right characters respectively
        # Append left index to r
        r = []
        d = [0] * 26
        for x in p:
            d[ord(x) - ord('a')] += 1
        left, right = 0, len(p)-1
        ss = s[left:right+1]
        w = [0] * 26
        for x in ss:
            w[ord(x) - ord('a')] += 1
        while right < len(s):
            if d == w:
                r.append(left)
            w[ord(s[left]) - ord('a')] -= 1
            right += 1
            if right < len(s):
                w[ord(s[right]) - ord('a')] += 1
            left += 1
        return r
