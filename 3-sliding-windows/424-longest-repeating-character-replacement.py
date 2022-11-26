# -----------------------------------------------------------
# 424. Longest Repeating Character Replacement
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
# Example 1:
#   Input: s = "ABAB", k = 2
#   Output: 4
#   Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:
#   Input: s = "AABABBA", k = 1
#   Output: 4
#   Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
#   The substring "BBBB" has the longest repeating letters, which is 4.
# -----------------------------------------------------------
from typing import List

# Inital Solution
# O(mn) time where m is the number of unique characters and n is the length of the string
# Slow sliding window


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end, highest, count = 0, 0, 0, 0
        # window capture section of same char string
        # go down, with tolerance of k times
        # store highest and go back to first time its different
        #   dictionary to store first time

        a = [0] * 26
        for x in s:
            if a[ord(x) - ord("A")] == 0:
                a[ord(x) - ord("A")] = 1

        for ind, n in enumerate(a):
            if n == 0:
                continue
            i = chr(ord("A") + ind)
            count = 0
            end = 0
            start = 0
            while end < len(s):
                # case where you continue the trek since same char
                highest = max(highest, end-start)
                if s[end] == i:
                    end += 1
                else:
                    # if we havent used up all k
                    if count < k:
                        end += 1
                        count += 1
                        continue
                    else:
                        # first save highest value
                        while start < end and count >= k:
                            if s[start] != i:
                                count -= 1
                            start += 1
                        if start == end:
                            start += 1
                            end += 1
            highest = max(highest, end-start)
        return highest
