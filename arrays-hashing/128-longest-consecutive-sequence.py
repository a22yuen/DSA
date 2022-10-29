# -----------------------------------------------------------
# 128. Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
# Example 1:
#   Input: nums = [100,4,200,1,3,2]
#   Output: 4
#   Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:
# 	Input: nums = [0,3,7,2,5,8,4,6,0,1]
# 	Output: 9
# -----------------------------------------------------------

# Hashset the numbers to make them O(1) access. For each number, check if the next one exists
# O(n) time since the while loop inside is restricted to the possible elements inside nums, ie at most n runs
# This gives O(n + n) = O(n)
class Solution:
  def longestConsecutive(self, nums) -> int:
			s = set(nums)
			highest = 1
			curn = 0
			curs = 1
			for x in nums:
				curn = x
				while curn + 1 in s:
					curn += 1
					curs += 1
				if highest < curs:
					highest = curs
				curs = 1
			return highest

x = Solution()
print(x.longestConsecutive([100,4,200,1,3,2]))
