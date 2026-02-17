# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Curr = head
        prev = None
        while Curr:
            temp = Curr.next
            Curr.next=prev
            prev = Curr
            Curr=temp
        return prev

     
        