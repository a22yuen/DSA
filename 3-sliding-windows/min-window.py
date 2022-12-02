from typing import List
import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # We want to track the highest value within a window, and we don't want to revisit characters
        # We also need the next highest number when the highest number leaves the window
        # This calls for a deque, to access the highest and append new values from the back
 
        # Removes old item if necessary, and adds new element i while maintaining decreasing order
        def clear_dq(i):
            # if first item in dq no longer in window, using k to track window size, no need for left pointer
            if dq and dq[0] == i - k:
                dq.popleft()
            
            # This ensures monotonic decreasing deque by removing all values smaller than the current one
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)

        # base cases
        if len(nums) * k == 0:
            return []	
        if k == 1:
            return nums
        dq = collections.deque([0])
        # prep dq with first window, keeping highest decreasing order
        for i in range(1,k):
            clear_dq(i)
        r=[nums[dq[0]]]
        # During each shift, update dq wiht clear_dq, and add the highest value
        for i in range(k, len(nums)):
            clear_dq(i)
            r.append(nums[dq[0]])
        return r