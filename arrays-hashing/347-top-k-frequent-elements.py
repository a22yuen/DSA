# -----------------------------------------------------------
# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Example 1:
#   Input: nums = [1,1,1,2,2,3], k = 2
#   Output: [1,2]
# Example 2:
#   Input: nums = [1], k = 1
#   Output: [1]
# -----------------------------------------------------------

# i love python syntax
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # dictionary to count number of each element
        count = collections.Counter(nums)
        # sort dictionary in descending order by value
        s = sorted(count, key=count.__getitem__, reverse=True)
        # return first k elements
        return s[:k]


# Less than O(nlogn)

# Heap
# get counter of all numbers -> insert into heap -> return first k elements
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == len(nums):
            return nums

        count = collections.Counter(nums)
        h = [(-v, key) for key, v in count.items()]
        heapq.heapify(h)
        r = []
        for i in range(k):
            v, key = heapq.heappop(h)
            r.append(key)
        return r

# bucket sort (idk)
