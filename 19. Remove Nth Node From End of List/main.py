# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode()
        dummy.next = head

        fast = dummy
        for i in range(n + 1):
            fast = fast.next
            if fast is None:
                return head.next

        slow = dummy
        while fast:
            fast = fast.next
            slow = slow.next

        print(slow.val)
        slow.next = slow.next.next

        return dummy.next
