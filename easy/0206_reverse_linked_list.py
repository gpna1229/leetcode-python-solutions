# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Recursion
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        else:
            self.reverseList(head.next)  
            return head      

# Iteration
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        new_head = None
        while curr:
            tmp = curr.next
            curr.next = new_head
            new_head = curr
            curr = tmp 
        return new_head
