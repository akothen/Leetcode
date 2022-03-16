
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

    
    
# Question: You are given the head of a linked list, and an integer k.
# Return the head of the linked list after swapping the values of the kth node 
# from the beginning and the kth node from the end (the list is 1-indexed).
# Link: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
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
        node_list = []
        curr_node = head
        while curr_node != None:
            node_list.append(curr_node)
            curr_node = curr_node.next
        if k > len(node_list):
            return head
        node_list_len = len(node_list)
        if node_list_len == 1:
            return head
        if k == 1:
            if node_list_len > 2:
                node_list[node_list_len - 1].next = node_list[0].next
                node_list[node_list_len - 2].next = node_list[0]
            else:
                node_list[node_list_len - 1].next = node_list[0]
            node_list[0].next = None
            head = node_list[node_list_len - 1]
        elif k - 1 != node_list_len - k:
            node_list[node_list_len - k - 1].next = node_list[k - 1]
            node_list[k - 1].next = node_list[node_list_len - k].next
            node_list[node_list_len - k].next = node_list[k]
            node_list[k - 2].next = node_list[node_list_len - k]
        return head
        
        
   


    
# Question: You are given the head of a linked list. Delete the middle node, 
# and return the head of the modified linked list.
# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the 
# start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
# Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# My solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        node_list = []
        curr_node = head
        while curr_node != None:
            node_list.append(curr_node)
            curr_node = curr_node.next
        node_list_len = len(node_list)
        if node_list_len == 1:
            return None
        if node_list_len % 2 == True:
            index = int(node_list_len / 2)
            if node_list_len == 2:
                node_list[index - 1].next = None
            else:
                node_list[index - 1].next = node_list[index + 1]
            node_list[index].next = None
        else:
            index = int(floor(node_list_len / 2))
            node_list[index - 1].next = node_list[index + 1]
            node_list[index].next = None
        return head
