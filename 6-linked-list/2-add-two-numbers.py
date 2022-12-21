class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        one = l1
        two = l2
        d = ListNode(0)
        curr = d
        carry = 0
        while one or two:
            s1 = 0
            s2 = 0
            if one:
                s1 = one.val
                one = one.next
            if two:
                s2 = two.val
                two = two.next
            s = s1 + s2 + carry
            if s > 9:
                curr.next = ListNode(s % 10)
                carry = 1
            else:
                curr.next = ListNode(s)
                carry = 0
            curr = curr.next
        if carry:
            curr.next = ListNode(1)
        return d.next
