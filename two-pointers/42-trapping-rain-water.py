# -----------------------------------------------------------
# 42. Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# Example 1:
#   Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
#   Output: 6
#   Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:
#   Input: height = [4,2,0,3,2,5]
#   Output: 9
# -----------------------------------------------------------

from typing import List
# Initial Solution
# V1: Doesn't account for buckets inside buckets
# V2: accounts for buckets in buckets, but O(n^2) when going back to tally heights
# need to keep track while going down list

# V3: 2 pointer, O(1) space complexity LETS GOOO
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = 0
        total = 0
        while l < len(height)-1 and r < len(height):
            # search for start left side of bucket
            if height[l] <= height[l+1]:
                l += 1
                continue
            # search for second side of bucket
            r = l+2
            while r < len(height):
                if height[r-1] < height[r]:
                    # we have water!
                    if height[r-1] > height[l] and height[r] > height[l]:
                        # both taller than highest, need better highest
                        l = r
                        r = l+2
                        continue
                    elif height[l] > height[r]:
                        # not taller than highest
                        for i in range(r-1, l-1, -1):
                            if height[i] >= height[r]:
                                # found leftside bucket
                                for j in range(i+1, r):
                                    mh = i if height[i] < height[r] else r
                                    if height[mh] - height[j] < 0:
                                        return -2
                                    total += height[mh] - height[j]
                                    height[j] = height[mh]
                                break
                    elif height[l] <= height[r]:
                        for i in range(l+1, r):
                            total += height[l] - height[i]
                            height[i] = height[l]
                        l = r
                        break
                    else:
                        print("doom")
                        return -1
                r += 1
        return total
