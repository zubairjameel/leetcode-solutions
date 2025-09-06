class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def length(curr):
            count = 0
            while curr:
                count += 1
                curr = curr.next
            return count

        total = length(head)            
        target = total - n               

        dummy = ListNode(0, head)      
        cur = dummy

        for _ in range(target):
            cur = cur.next

        cur.next = cur.next.next

        return dummy.next
