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
    ret = []
    rev = [x for x in reversed(r)]
    for i in range(len(nums)):
        ret.append(l[i] * rev[i])
    return ret


# O(1) Space complexity, O(n) time complexity
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Each value in the resultant array is made of a products of all values at indexes < i, and product of values of index > i
        # Thus we can split our values into 2 different variables, left product and right product
        # Calculate left product by collecting the accumulative product from the left
        # We do the same for the right, by keeping an accumulative product from the right as a variable
        r = [1]
        for i in range(1, len(nums)):
            # left side products
            r.append(nums[i-1] * r[i-1])
        rhs = 1
        for i in range(len(nums)-2, -1, -1):
            # accumuate rhs and multiply into r
            rhs *= nums[i+1]
            r[i] *= rhs
        return r
