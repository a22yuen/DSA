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
from typing import List
import collections


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

# Optimal Solution, with deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # We want to track the highest value within a window, and we don't want to revisit characters
        # We also need the next highest number when the highest number leaves the window
        # This calls for a deque, to access the highest and append new values from the back

        # Removes old item if necessary, and adds new element i while maintaining decreasing order
        def clear_dq(i):
            # if first item in dq no longer in window, using k to track window size, no need for left pointer
            if dq and dq[0] == i - k:
                dq.popleft()

            # This ensures monotonic decreasing deque by removing all values smaller than the current one
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)

        # base cases
        if len(nums) * k == 0:
            return []
        if k == 1:
            return nums
        dq = collections.deque([0])
        # prep dq with first window, keeping highest decreasing order
        for i in range(1, k):
            clear_dq(i)
        r = [nums[dq[0]]]
        # During each shift, update dq wiht clear_dq, and add the highest value
        for i in range(k, len(nums)):
            clear_dq(i)
            r.append(nums[dq[0]])
        return r
