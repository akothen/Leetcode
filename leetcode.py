
# Question: Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)
# My solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        cur_node = head
        prev_node = None
        while cur_node != None:
            if prev_node == None:
                next_node = cur_node.next
                cur_node.next = next_node.next
                next_node.next = cur_node
                head = next_node
            else:
                prev_node.next = cur_node.next
                cur_node.next = prev_node.next.next
                prev_node.next.next = cur_node
            prev_node = cur_node
            cur_node = prev_node.next
        return head
