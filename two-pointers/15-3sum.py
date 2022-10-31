# -----------------------------------------------------------
# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
#   Input: nums = [-1,0,1,2,-1,-4]
#   Output: [[-1,-1,2],[-1,0,1]]
#   Explanation: 
#       nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 \= 0.
#       nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
#       nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
#       The distinct triplets are [-1,0,1] and [-1,-1,2].
#       Notice that the order of the output and the order of the triplets does not matter.
# Example 2:
#   Input: nums = [0,1,1]
#   Output: []
#   Explanation: The only possible triplet does not sum up to 0.
# Example 3:
#   Input: nums = [0,0,0]
#   Output: [[0,0,0]]
#   Explanation: The only possible triplet sums up to 0.
# -----------------------------------------------------------
class Solution:
    class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = collections.defaultdict(list)
        r = set()
        for i, x in enumerate(nums):
            if len(d[x]) == 3:
                continue
            d[x].append(i)
        print(d.items())
        for ind1,x in enumerate(nums):
            if len(d[x]) == 3 and d[x][-1] < ind1:
                continue
            for ind2, y in enumerate(nums):
                if ind2 == ind1:
                    continue
                search = -(x + y)
                if search in d:
                    for ind3 in d[search]:
                        if ind3 != ind2 and ind3 != ind1:
                            r.add(tuple(sorted([x,y,search])))
                            break
        return r
    