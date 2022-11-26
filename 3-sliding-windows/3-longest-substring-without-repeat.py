# -----------------------------------------------------------
# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
#   Input: s = "abcabcbb"
#   Output: 3
#   Explanation: The answer is "abc", with the length of 3.
# Example 2:
#   Input: s = "bbbbb"
#   Output: 1
#   Explanation: The answer is "b", with the length of 1.
# Example 3:
#   Input: s = "pwwkew"
#   Output: 3
#   Explanation: The answer is "wke", with the length of 3.
#   Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# -----------------------------------------------------------

import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Hash set to keep track of viewed values
        # When a value is in hashset, iterate from the back, removing values until you reach the end value
        # This leaves a string with no repeated characters!
        d = set()
        start, end, highest = 0, 0, 0
        while end < len(s):
            if s[end] in d:
                while start < end:
                    if s[start] == s[end]:
                        start += 1
                        break
                    d.remove(s[start])
                    start += 1
                highest = max(highest, end-start)
                end += 1
            else:
                d.add(s[end])
                end += 1
                highest = max(highest, end-start)
        return highest


# SUPER OPTIMAL SOLUTION WITH SAVING INDEX


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # When traversing unique character substring, when reaching a character already in substring,
        # the new substring you track must start after the first repeated character.
        # This can be done by jumping to index after the first repeated character.
        # Keep track of indices of visited characters
        # left goes to index after first instance of repeated character within the substring
        d = {}
        left, right, highest, curr = 0, 0, 0, 0
        while right < len(s):
            if s[right] not in d:
                d[s[right]] = right
                right += 1
            else:
                left = max(left, d[s[right]] + 1)
                d[s[right]] = right
                right += 1
            highest = max(highest, right-left)
        return highest
