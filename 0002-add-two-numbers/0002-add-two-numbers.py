# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c1 = l1
        t1 = 1
        s1 = 0
        while c1 != None:
            s1 = s1 + t1 * (c1.val)
            t1 = t1*10
            c1 = c1.next
        
        c2 = l2
        t2 = 1
        s2 = 0
        while c2 != None:
            s2 = s2 + t2 * (c2.val) 
            t2 = t2*10
            c2 = c2.next
        
        sum_num = s1 + s2
        new_head = ListNode(val = sum_num % 10, next = None)
        sum_num = (sum_num - (sum_num % 10))/10
        current = new_head
        while sum_num != 0:
            new_val = sum_num % 10
            sum_num = (sum_num - (new_val))/10
            new_node = ListNode(val = new_val, next = None)
            current.next = new_node
            current = current.next
        
        return new_head
