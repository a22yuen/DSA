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

# Optimal Solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Counter of frequency in array
        # We want a heap that will contain the k most frequent elements
        # To do this, we want a min heap of k size
        # We push k elements onto heap k logn
        # Then push pop n-k elements onto heap, removing the smallest value if there is a bigger one
        #   pushpop is faster than push and pop, logn vs 2logn
        # Return heap
        count = collections.Counter(nums)
        h = []
        newk = 0
        for key,v in count.items():
            if newk < k:
                heappush(h, (v,key))
                newk += 1
            else:
                if v > h[0][0]:
                    heappushpop(h, (v,key))
        r = [key for v,key in h]
        return r

# i love python syntax
# O(nlogn)
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        # sort dictionary in descending order by value
        s = [key for key, v in sorted(
            count.items(), key=lambda item: item[1], reverse=True)]
        # return first k elements
        return s[:k]


# Less than O(nlogn)

# Heap
# get counter of all numbers -> heapify -> return first k elements
# O(n + log(h) + klog(n)) where h is number of distinct elements in nums, h < n
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