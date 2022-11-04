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
# Doesn't account for buckets inside buckets
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = 0
        total = 0
        while r < len(height) and l < len(height)-1:
            # search for first side of bucket
            print("start left", l)
            if height[l] <= height[l+1]:
                if l >= len(height)-2:
                    return total
                l += 1
                continue
            # search for second side of bucket
            r = l+2
            while r < len(height) and height[r] < height[l]:
                print("find right", r)
                r += 1
            if r >= len(height):
                print("cant find")
                l += 1
                print("cant", l)
                r = l
                continue
            newl = l
            newr = r
            while newl < newr:
                print("newl", newl)
                print("newr", newr)
                diff = newr-newl-1
                total += diff
                newl = newl+1
                newr = newr-1
                
            l = r
        return total
            