"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(nums, left, right):
            if left > right:
                return -1
            
            mid = left + (right-left)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySearch(nums,left,mid-1)
            else:
                return binarySearch(nums, mid+1, right)
        
        return binarySearch(nums, 0, len(nums)-1)