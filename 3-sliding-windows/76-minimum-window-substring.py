# -----------------------------------------------------------
# 76. Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.
# Example 1:
#   Input: s = "ADOBECODEBANC", t = "ABC"
#   Output: "BANC"
#   Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:
#   Input: s = "a", t = "a"
#   Output: "a"
#   Explanation: The entire string s is the minimum window.
# Example 3:
#   Input: s = "a", t = "aa"
#   Output: ""
#   Explanation: Both 'a's from t must be included in the window.
#   Since the largest window of s only has one 'a', return empty string.
# -----------------------------------------------------------

# Bad Initial Implementation
class Solution:
    def i(self, c: str):
        return ord(c) - ord('A')

    def minWindow(self, s: str, t: str) -> str:
        # where s is the main string and t is the substring
        # i = ord(x) - ord('A')
        if len(t) > len(s):
            return ""
        left, right = 0, len(t)-1
        minstr = s
        sarr = [0] * 58
        tarr = [0] * 58
        for i in range(len(t)):
            sarr[self.i(s[i])] += 1
            tarr[self.i(t[i])] += 1
        matches = 0
        for i in range(58):
            if tarr[i] > 0 and sarr[i] > 0 and tarr[i] > 0:
                matches += min(sarr[i], tarr[i])
        while right < len(s):
            if matches == len(t):
                break
            right += 1
            if right < len(s):
                sarr[self.i(s[right])] += 1
                if tarr[self.i(s[right])] > 0 and sarr[self.i(s[right])] <= tarr[self.i(s[right])]:
                    matches += 1
        if matches != len(t):
            return ""
        while right < len(s):
            if matches == len(t):
                #  reduce window size
                minstr = s[left:right+1]
                if tarr[self.i(s[left])] > 0 and sarr[self.i(s[left])]-1 < tarr[self.i(s[left])]:
                    matches -= 1
                else:
                    minstr = s[left+1:right+1]
                sarr[self.i(s[left])] -= 1
                left += 1
                continue
            # smaller window that fails
            right += 1
            if right < len(s):
                sarr[self.i(s[left])] -= 1
                if tarr[self.i(s[left])] > 0 and sarr[self.i(s[left])] < tarr[self.i(s[left])]:
                    matches -= 1
                sarr[self.i(s[right])] += 1
                if tarr[self.i(s[right])] > 0 and sarr[self.i(s[right])] <= tarr[self.i(s[right])]:
                    matches += 1
                left += 1
        return minstr
