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

      
      
