class Solution(object):
    def reverseKGroup(self, head, k):

        dummy = ListNode(0)
        dummy.next = head
        current = head
        length = 0
        while current:
            length += 1
            current = current.next

        before = dummy
        origin = head
        slow = origin
        fast = slow.next if slow else None

        while length >= k:
            nodes_to_move = k - 1

            while nodes_to_move > 0:
                slow.next = fast.next
                fast.next = origin
                origin = fast
                before.next = origin
                fast = slow.next
                nodes_to_move -= 1

            before = slow
            origin = fast
            slow = origin
            fast = slow.next if slow else None
            length -= k

        return dummy.next
