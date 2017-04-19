# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 21:15:28 2017

@author: zhang_000
"""

# search in rotated array
def search(nums, target):
    if not nums:
        return -1
    idx = locateRotateIdx(nums)
    if idx == 0:
        return binarySearch(nums, target)
    if target <= nums[idx - 1]:
        return binarySearch(nums[:idx], target)
    else:
        return idx + binarySearch(nums[idx:], target)
    
def locateRotateIdx(nums):
    left = 0
    right = len(nums) - 1
    while right > left:
        print right
        print left
        mid = left + (right - left)/2
        if nums[mid] >= nums[right]:
            left = mid + 1
        else:
            right = mid - 1
    if nums[left] > nums[right]:
        return left
    else:
        return right        
 
def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1
    while right >= left:
        mid = left + (right - left)/2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1        
        
            
        