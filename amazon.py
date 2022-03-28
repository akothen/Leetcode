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
            
            
    
      
      
