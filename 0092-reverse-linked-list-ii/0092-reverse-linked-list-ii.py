# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not head:
            return

        dummy = leftprev = ListNode(next=head)
        curr = head

        for _ in range(left - 1):
            leftprev = leftprev.next

        curr = leftprev.next
        prev = None

        for _ in range(right-left + 1):
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp

        leftprev.next.next = curr
        leftprev.next = prev
        return dummy.next
