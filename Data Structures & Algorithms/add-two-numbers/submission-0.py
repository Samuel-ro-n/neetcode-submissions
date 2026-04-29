# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode(0)
        current= dummy
        carry=0
        while l1 or l2 or carry:
            Sum= l1.val + l2.val + carry
            fsum= Sum % 10
            carry= Sum//10
            current.next= ListNode(fsum)
            l1= l1.next
            l2= l2.next
            current= current.next
        return dummy.next
        