# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        curr=second
        prev=None
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        
        list1=head
        list2=prev

        while list1 and list2:
            firstend=list1.next
            secondend=list2.next

            list1.next=list2
            list2.next=firstend

            list1=firstend
            list2=secondend
        
        

