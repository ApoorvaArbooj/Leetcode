def searchInsert(nums,target) -> int:
  
  #Initializing variables
  left, right = 0, len(nums) - 1
  
  while left <= right:
    #Find the mid point
    pivot = (left + right) // 2
    #If the target is found in the centre return it
    if nums[pivot] == target:
      return pivot
    #If target is less than the middle/pivot value 
    #than search only in the left section of the input list
    if target < nums[pivot]:
      right = pivot - 1
    #If target is less than the middle/pivot value 
    #than search only in the right section of the input list
    else:
      left = pivot + 1
      
  return left

nums = [1,3,5,7]
target = 6

# Note: List index starts from 0
print(f'The target = {target} can be inserted in the {searchInsert(nums,target)} position of the input list.')

