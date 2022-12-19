"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# 2 pass, hash map to keep association between og and copy


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        curr = Node(head.val)
        m = {}
        og = head.next
        prev = head
        while og:
            curr.next = Node(og.val)
            m[prev] = curr
            prev = og
            og = og.next
            curr = curr.next
        m[prev] = curr
        og = head
        curr = m[head]
        while curr:
            if og.random:
                curr.random = m[og.random]
            curr = curr.next
            og = og.next
        return m[head]

# 1 pass visited dictionary, going through both random and next recursively

# 1 pass O(1) space, using copy of node as next node, to keep association between og and copy
