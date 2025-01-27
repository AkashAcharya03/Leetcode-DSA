# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        head=dummy
        current1 =l1
        current2=l2
        carry=0
        while current1 is not None or current2 is not None:
            sum=0
            if current1 is not None:

                sum=sum+current1.val
                current1 =current1.next
            if current2 is not None:
                sum=sum+current2.val
                current2 =current2.next
            sum=sum+carry
            carry=0
            if sum>9:
                sum=sum%10
                carry=1
            head.next=ListNode(sum)
            head=head.next
        if carry!=0:
            head.next=ListNode(carry)
            head=head.next

         
        return(dummy.next)

            
