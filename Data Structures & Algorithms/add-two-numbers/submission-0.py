# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #we need to add these values
        #if its double digit we need to have the end value then remainder which is tens digit in the carry
        #first we have to check if the list1 is not null if its we make it 0 also it goes here only if we have any of the list and carry left once we get the answer we create a newnode and add it to dummy we are not putting out list in dummy we are creating a new one 
        dummy=ListNode(9)
        tail=dummy

        carry=0

        while carry or l1 or l2:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0

            total=val1+val2+carry

            digit=total%10
            carry=total//10

            newnode=ListNode(digit)
            tail.next=newnode
            tail=tail.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next
                









