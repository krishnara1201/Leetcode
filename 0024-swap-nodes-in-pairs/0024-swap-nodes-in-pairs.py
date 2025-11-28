# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        if not head.next:
            return head

        n1, n2 = head, head.next
        prev = dummy = ListNode(next=n1)

        while n1 and n2:
            temp = n2.next
            n2.next = n1
            n1.next = temp
            prev.next = n2
            prev = n1
            if temp and temp.next:
                n1 = temp
                n2 = temp.next
            else:
                break
            
        
        return dummy.next


        