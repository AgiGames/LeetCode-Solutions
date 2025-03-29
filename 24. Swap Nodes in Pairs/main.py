# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        dummy = ListNode(0)
        dummy.next = head
        origin = dummy

        slow = head

        if head is not None:
            fast = head.next
        else:
            fast = None

        while slow and fast:
            slow.next = fast.next
            fast.next = slow
            origin.next = fast
            
            origin = slow
            if slow.next is not None:
                fast = slow.next.next
            else:
                fast = None
            slow = slow.next

        return dummy.next
