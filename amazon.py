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
                    
 
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack
# Link: https://leetcode.com/problems/min-stack/
class MinStack:
    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min == None:
            self.min = val
        elif self.min > val:
            self.min = val

    def pop(self) -> None:
        elem = self.stack.pop()
        if elem == self.min:
            if len(self.stack) != 0:
                self.min = self.stack[0]
                for val in self.stack[1:]:
                    if val < self.min:
                        self.min = val
            else:
                self.min = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()




# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. 
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds the 
# capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.
# Link: https://leetcode.com/problems/lru-cache/
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value
        self.cache.move_to_end(key)
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)





# Given the head of a linked list, rotate the list to the right by k places.
# Link: https://leetcode.com/problems/rotate-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        if k == 0:
            return head
        node_list = list()
        node = head
        while node != None:
            node_list.append(node)
            node = node.next
        if len(node_list) == 1:
            return head
        if k % len(node_list) == 0:
            return head
        rot = k % len(node_list)
        length = len(node_list)
        node_list[length - 1].next = head
        node_list[length - rot - 1].next = None
        head = node_list[length - rot]
        return head
        
        
            
        
