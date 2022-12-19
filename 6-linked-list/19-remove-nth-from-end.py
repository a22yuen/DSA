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

# Solution with dummy node, Won't need prev or check if head is None


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(0)
        d.next = head
        slow = d
        fast = d
        prev = None
        for i in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return d.next
