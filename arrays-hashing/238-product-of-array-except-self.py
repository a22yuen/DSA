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

# Solution 1: 2 array for left and right.
# Each number in the solution can be broken down to product of prefix * product of suffix
# Thus, create 1 array for prefix (left) and 1 array for suffix (right)
def lrarr(nums):
    l = [1]
    r = [1]
    for i in range(len(nums)-1):
        l.append(nums[i] * l[i])
    i = 0
    rev = [x for x in reversed(nums)]
    for i in range(len(nums)-1):
        r.append(rev[i] * r[i])
    ret=[]
    rev = [x for x in reversed(r)]
    for i in range(len(nums)):
        ret.append(l[i] * rev[i])
    return ret

# O(1) space complexity
# make left pass accumulated product array in r. Go backwards and multiply by v, where v is the accumulated product of the right pass
# using variables to store state if you only need the state at a given time
class Solution:
    def productExceptSelf(self, nums):
        r = [1]
        for i in range(1, len(nums)):
            r.append(r[i-1]*nums[i-1])

        v = 1
        for i in range(len(nums)-1, -1, -1):
            r[i] *= v
            v *= nums[i]
        return r
