# Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution(object):
  def maxSubArray(self, nums):
      c = 0
      m = float('-inf')
      for i in nums:
          c = c + i
          m = max(c, m)
          if c < 0:
              c = 0
      return m

if __name__ == "__main__":
  solution = Solution()
  nums = list(map(int, input("Enter the elements of the array, separated by spaces: ").split()))
  print("Max subarray sum:", solution.maxSubArray(nums))
