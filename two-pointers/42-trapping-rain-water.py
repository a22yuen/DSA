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

# Initial Solution
# V1: Doesn't account for buckets inside buckets
# V2: accounts for buckets in buckets, but O(n^2) when going back to tally heights
# need to keep track while going down list
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = 0
        total = 0
        while r < len(height) and l < len(height)-1:
            # search for first side of bucket
            if height[l] <= height[l+1]:
                if l >= len(height)-2:
                    return total
                l += 1
                continue
            # search for second side of bucket
            r = l+2
            poss = -1
            while r < len(height) and height[r] < height[l]:
                if height[r-1] < height[r]:
                    if poss == -1:
                        poss = r
                    elif height[poss] < height[r]:
                        poss = r
                r += 1
            if r >= len(height):
                if poss == -1:
                    l += 1
                    r = l
                    continue
                else:
                    r = poss
            mh = min(height[r], height[l])
            i = l+1
            while i < r:
                total += max(0,mh - height[i])
                i += 1
            l = r
        return total
            
            