# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        if len(lists) == 0:
            return None

        low = 0
        high = len(lists) - 1

        def mergeTwoLists(list1, list2):

            dummy = ListNode(0)
            ptr = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    ptr.next = list1
                    list1 = list1.next

                else:
                    ptr.next = list2
                    list2 = list2.next

                ptr = ptr.next

            ptr.next = list1 if list1 else list2

            return dummy.next

        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists) - 1, 2):
                merged_lists.append(mergeTwoLists(lists[i], lists[i + 1]))

            if len(lists) % 2 == 1:
                merged_lists.append(lists[-1])

            lists = merged_lists
            print(len(merged_lists))

        return lists[0]
