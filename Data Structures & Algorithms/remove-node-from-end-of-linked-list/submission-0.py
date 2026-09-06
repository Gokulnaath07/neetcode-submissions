# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #we are going to use two pointer technique by starting the one node n times ahead of the value so when the value becomes none for that ahead pointer then the slow pointer will be before that value because once we moved that fast pointer two stepss we will be moving both fast and slow at same pace i per time but slow goes first its like slow trying to catch up 

        dummy=ListNode(0)
        dummy.next=head


        fast=dummy
        slow=dummy
        for _ in range(n+1):
            fast=fast.next
        while fast:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return dummy.next




        