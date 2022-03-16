
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

    

# Question: Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# My solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return None
        node_list = []
        curr_node = head
        while curr_node != None:
            node_list.append(curr_node)
            curr_node = curr_node.next
        if n > len(node_list):
            return head
        node_list_len = len(node_list)
        if n == 1:
            node_list[node_list_len - 2].next = None
        elif n == node_list_len:
            head = node_list[1]
        else:
            node_list[node_list_len - n - 1].next = node_list[node_list_len - n + 1]
            node_list[node_list_len - n].next = None
        return head
