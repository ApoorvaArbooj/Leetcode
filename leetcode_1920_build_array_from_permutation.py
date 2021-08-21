
def buildArray(nums):
  ans = []
  for i in range(len(nums)):
    ans.append(nums[nums[i]])
  return ans

#Input: nums = [0,2,1,5,3,4]
#Output: [0,1,2,4,5,3]

nums1 = [0,2,1,5,3,4]

print(f'Input: nums = {nums1}\nOutput: {buildArray(nums1)}')

