# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        slow = mid
        # reverse second half of list
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        mid = prev
        # merge
        start = head
        while start and mid:
            next_o = start.next
            next_mid = mid.next
            mid.next = next_o
            start.next = mid
            mid = next_mid
            start = next_o
        return head
