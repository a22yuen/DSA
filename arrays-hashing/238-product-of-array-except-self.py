# -----------------------------------------------------------
# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
# Example 1:
#   Input: nums = [1,2,3,4]
#   Output: [24,12,8,6]
# Example 2:
#   Input: nums = [-1,1,0,-3,3]
#   Output: [0,0,9,0,0]
# -----------------------------------------------------------


# O(1) space complexity
# make left pass accumulated product array in r. Go backwards and multiply by v, where v is the accumulated product of the right pass
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = [1]
        for i in range(1, len(nums)):
            r.append(r[i-1]*nums[i-1])

        v = 1
        for i in range(len(nums)-1, -1, -1):
            r[i] *= v
            v *= nums[i]
        return r
