# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        current1 = list1
        current2 = list2
        while current1 and current2:
            if current1.val < current2.val:
                head.next = current1
                current1 = current1.next
            else:
                head.next = current2
                current2 = current2.next
            head=head.next

        if current1:
            head.next=current1
        else:
            head.next=current2

        return dummy.next
