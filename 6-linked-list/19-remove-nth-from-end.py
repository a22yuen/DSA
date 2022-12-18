# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = None
        for i in range(n):
            fast = fast.next
        while fast:
            prev = slow
            fast = fast.next
            slow = slow.next
        if prev:
            prev.next = slow.next
        else:
            head = head.next
        return head
