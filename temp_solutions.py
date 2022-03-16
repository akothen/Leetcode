
# Question: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# My solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        # Add the nodes of the linked list in a list
        node_list = []
        cur_node = head
        while cur_node != None:
            node_list.append(cur_node)
            cur_node = cur_node.next
        # Swap nodes of the linked list
        tmp_node1 = node_list[k-1]
        tmp_node2 = node_list[len(node_list) - k - 1]
        if tmp_node1 == tmp_node2:
            return head
        if k != 1:
            node_list[k-2].next = tmp_node2
            tmp_node2.next = node_list[k+1]
            node_list[len(node_list) - k - 2].next = tmp_node1
        else:
            tmp_node2.next = node_list[k+1]
            node_list[len(node_list) - k - 2].next = tmp_node1
            head = tmp_node2
        tmp_node1.next = node_list[len(node_list) - k]
        return head
        
        
        
