# Given an array of integers nums and an integer target, return indices 
# of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you 
# may not use the same element twice.
# You can return the answer in any order.
# Link: https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx in range(len(nums)):
            for next_idx in range(idx + 1, len(nums)):
                if nums[idx] + nums[next_idx] == target:
                    return [idx, next_idx]
        return None

    
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# Link: https://leetcode.com/problems/add-two-numbers/
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNumber(node : Optional[ListNode]) -> int:
            num = 0
            scale = 1
            while node != None:
                num += (scale * node.val)
                scale *= 10
                node = node.next
            return num
        num1 = getNumber(l1)
        num2 = getNumber(l2)
        sum = num1 + num2
        print(sum)
        scale = 10
        cur_node = None
        start = None
        while sum != 0:
            sum_string = repr(sum)
            last_digit = sum_string[-1]
            print(sum_string[:-1])
            if len(sum_string) != 1:
                sum = int(sum_string[:-1])
            else:
                sum = 0
            print(sum)
            if cur_node == None:
                start = ListNode(int(last_digit))
                cur_node = start
            else:
                cur_node.next = ListNode(int(last_digit))
                cur_node = cur_node.next
        if start == None:
            return ListNode(sum)
        return start
            
 
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it. 
# Link: https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def printList(list1):
            print("PRINTING LIST:")
            node = list1
            while node != None:
                print(node.val)
                node = node.next
            
        def insertlistinto(list1, list2):
            head1 = list1
            head2 = list2
            cur_node2 = head2
            while cur_node2 != None:
                cur_node1 = head1
                prev_node1 = None
                while cur_node1 != None and cur_node1.val < cur_node2.val:
                    prev_node1 = cur_node1
                    cur_node1 = cur_node1.next
                head2 = cur_node2.next
                cur_node2.next = cur_node1
                if head1 == cur_node1:
                    head1 = cur_node2
                else:
                    prev_node1.next = cur_node2
                cur_node2 = head2
            return head1
        
        def merge2Lists(list1 : Optional[ListNode], list2 : Optional[ListNode]) -> Optional[ListNode]:
            if list1.val > list2.val:
                return insertlistinto(list2, list1)
            return insertlistinto(list1, list2)
        
        if len(lists) == 0:
            return None
        index = 0
        result = None
        for array in lists:
            if array == None:
                index += 1
                continue
            result = lists[index]
            break
        if index != len(lists) - 1:
            for array in lists[index + 1:]:
                if array == None:
                    continue
                result = merge2Lists(result, array)
        return result
                    
      
      