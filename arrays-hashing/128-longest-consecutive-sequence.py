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
	# 1. gather all distinct numbers in nums ( n time )
	# 2. go down nums and for each character search for the next character constant time for searching set
	# 3. each number we start searching must necessarily be the start of a chain, else there is a longer chain already that it is a part of. check if previous number exists
	# 4. no then iterate array, yes then follow 
		s = set(nums)
		highest = 0
		for x in nums:
			# check if chain starter
			if x-1 in s:
				continue
			# chain start
			curv = x
			curs = 1
			while curv in s:
				if curv+1 in s:
					curv += 1
					curs += 1
				else:
					break
			if curs > highest:
				highest = curs
		return highest

x = Solution()
print(x.longestConsecutive([100,4,200,1,3,2]))
